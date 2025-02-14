from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 

@dataclass(frozen =True)
class DataValidationconfig:
    root_dir:Path
    status_file:str
    unzip_dir:Path
    all_schema:dict