from flask import Flask, render_template, request, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
SCREENSHOT_FOLDER = 'screenshot'

@app.route('/screenshot/<path:filename>')
def serve_image(filename):
    return send_from_directory(SCREENSHOT_FOLDER, filename)


def group_images(images):
    grouped = {}

    for image in images:
        try:
            timestamp_str = image.split('_')[1] + image.split('_')[2].split('.')[0]
            timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
        except:
            continue

        month_key = timestamp.strftime('%B %Y')
        day_key = timestamp.strftime('%A, %d %B %Y')

        if month_key not in grouped:
            grouped[month_key] = {}
        if day_key not in grouped[month_key]:
            grouped[month_key][day_key] = []
        grouped[month_key][day_key].append(image)

    return grouped


@app.route('/')
def index():
    date_filter = request.args.get('date')
    month_filter = request.args.get('month')

    images = []
    for filename in os.listdir(SCREENSHOT_FOLDER):
        if filename.endswith(('.jpg', '.png')):
            try:
                timestamp_str = filename.split('_')[1] + filename.split('_')[2].split('.')[0]
                timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
            except:
                continue

            show = True
            if date_filter:
                selected_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
                show = timestamp.date() == selected_date
            elif month_filter:
                selected_month = datetime.strptime(month_filter, '%Y-%m')
                show = timestamp.year == selected_month.year and timestamp.month == selected_month.month

            if show:
                images.append(filename)

    images.sort(reverse=True)
    grouped = group_images(images)
    return render_template('index.html', grouped=grouped, date_filter=date_filter, month_filter=month_filter)


if __name__ == '__main__':
    app.run(debug=True)