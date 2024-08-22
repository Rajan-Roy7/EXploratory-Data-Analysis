from pydantic import BaseModel
from typing import List, Optional

class PreprocessRequest(BaseModel):
    numerical_cols: Optional[List[str]] = None
    categorical_cols: Optional[List[str]] = None
    encoding_type: Optional[str] = None
    missing_values_strategy: Optional[str] = None
    missing_categorical_strategy: Optional[str] = None
    normalization_strategy: Optional[str] = None
    outlier_n: Optional[int] = None
    outlier_features: Optional[List[str]] = None
