# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FileUploadCallbackRequest(DaraModel):
    def __init__(
        self,
        call_from: str = None,
        dms_unit: str = None,
        file_size: int = None,
        filename: str = None,
        oss_bucket: str = None,
        upload_location: str = None,
    ):
        # For frontend use only.
        self.call_from = call_from
        # The current DMS unit.
        self.dms_unit = dms_unit
        # The file size in bytes.
        self.file_size = file_size
        # The file name.
        # 
        # This parameter is required.
        self.filename = filename
        self.oss_bucket = oss_bucket
        # The full path for the file upload.
        # 
        # - Format: This path is formed by appending the file name to the UploadDir value returned by the DescribeFileUploadSignature operation.
        # 
        # - Example: ${UploadDir}/${Filename}
        # 
        # This parameter is required.
        self.upload_location = upload_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_from is not None:
            result['CallFrom'] = self.call_from

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.upload_location is not None:
            result['UploadLocation'] = self.upload_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFrom') is not None:
            self.call_from = m.get('CallFrom')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('UploadLocation') is not None:
            self.upload_location = m.get('UploadLocation')

        return self

