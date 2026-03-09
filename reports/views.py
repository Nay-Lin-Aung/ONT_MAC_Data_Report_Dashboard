from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse

REPORT_FOLDER = os.path.join(settings.BASE_DIR, "REPORT_FILES")

def dashboard(request):

    ont_reports = []
    mac_reports = []

    for file in os.listdir(REPORT_FOLDER):

        if "ONT_DATA_REPORT" in file:
            ont_reports.append(file)

        elif "MAC_ADDRESS_REPORT" in file:
            mac_reports.append(file)

    context = {
        "ont_reports": sorted(ont_reports, reverse=True),
        "mac_reports": sorted(mac_reports, reverse=True),
    }

    return render(request, "reports/dashboard.html", context)


def download_report(request, filename):

    file_path = os.path.join(REPORT_FOLDER, filename)

    return FileResponse(open(file_path, 'rb'), as_attachment=True)