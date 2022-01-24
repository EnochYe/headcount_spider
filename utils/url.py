def get_url(job_type, job_start):
    url = "https://www.linkedin.com/jobs/search/?" + job_type + "geoId=103644278&keywords=healthcare%20data%20analyst" \
                                                                "&location=United" \
                                                                "%20States&start=" + str(job_start)
    return url