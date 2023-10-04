import downloader

query = input("Enter the search query: ")
downloader.download(
    query, 
    limit=10,  
    output_dir='dataset', 
    adult_filter_off=False, 
    force_replace=False, 
    timeout=60, 
    verbose=True
)
