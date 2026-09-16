# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetadataSchemaField(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
        value_mode: str = None,
    ):
        # The name of the metadata field.
        self.name = name
        # Valid values: STRING, LONG, DOUBLE, BOOLEAN, and DATETIME. This field is ignored when ValueMode is set to SYSTEM_VARIABLE. The system enforces the inherent type of the bound variable: DOCUMENT_NAME, FILE_TYPE, SOURCE_TYPE, and SOURCE_URI use STRING. FILE_SIZE, DOCUMENT_UPLOAD_TIME, and SOURCE_MODIFIED_TIME use LONG. An incorrect value specified by the user has no effect.
        self.type = type
        # When ValueMode is set to CONSTANT, this field specifies a fixed value. An empty value indicates that the value can be assigned during document upload. When ValueMode is set to SYSTEM_VARIABLE, this field specifies a system variable name. Valid system variable names: DOCUMENT_NAME, FILE_TYPE, FILE_SIZE, DOCUMENT_UPLOAD_TIME, SOURCE_TYPE, SOURCE_URI, and SOURCE_MODIFIED_TIME. The system maintains the values of system variables. For manual uploads, the source is fixed to UPLOAD, and SOURCE_URI and SOURCE_MODIFIED_TIME use the values declared by the user. For event stream imports, the system automatically maintains the values. For example, for an OSS import, the source is OSS, SOURCE_URI is oss://bucket/key, and SOURCE_MODIFIED_TIME is the object modification time.
        self.value = value
        # This field is optional. If omitted, the user assigns the value during document upload. Valid values:
        # - CONSTANT: The field uses a constant. If Value is not empty, the fixed value is automatically applied to the document. If Value is empty, the value can be assigned during upload.
        # - SYSTEM_VARIABLE: The field is bound to a system variable. Value specifies the variable name, and the system automatically populates the value from the document facts.
        # 
        # A value explicitly provided by the user during document upload always takes precedence. The backend does not override user-specified values.
        self.value_mode = value_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_mode is not None:
            result['ValueMode'] = self.value_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueMode') is not None:
            self.value_mode = m.get('ValueMode')

        return self

