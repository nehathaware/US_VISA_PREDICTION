from dataclasses import dataclass

# gives return type


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 

