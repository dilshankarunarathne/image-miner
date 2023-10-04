import downloader


downloader.download(
    "cat", 
    limit=2,  
    output_dir='dataset', 
    adult_filter_off=True, 
    force_replace=False, 
    timeout=60, 
    verbose=True
)
