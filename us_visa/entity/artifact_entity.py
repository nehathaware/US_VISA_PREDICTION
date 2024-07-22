from dataclasses import dataclass

# gives return type


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path: str

