# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CreateDocParserJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        file_format: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        image_mode: str = None,
        oss_file_url: str = None,
        output_format: str = None,
        region_id: str = None,
        result_type: str = None,
        table_format: str = None,
    ):
        # The format of the input file. Valid values:
        # 
        # - **pdf**: PDF file.
        # 
        # - **docx**: Word file in docx format.
        # 
        # - **doc**: Word file in doc format.
        # 
        # - **pptx**: PPT file in pptx format.
        # 
        # - **ppt**: PPT file in ppt format.
        # 
        # - **txt**: plain text file.
        # 
        # - **md**: Markdown file.
        # 
        # - **png**: PNG image.
        # 
        # - **jpg**: JPG image.
        # 
        # - **jpeg**: JPEG image.
        # 
        # This parameter is required.
        self.file_format = file_format
        # The file name, which must include the file name extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The HTTP or HTTPS URL of the file to be parsed.
        # >SDKs for various languages provide an additional `CreateDocParserJobAdvance` method that supports passing a local file stream directly (such as InputStream in Java), without the need to upload the file to OSS and construct a FileUrl in advance. When using the Advance method, replace the `FileUrl` parameter (URL string) with the `FileUrlObject` parameter (file stream). All other request parameters remain unchanged. The SDK automatically performs the following operations:
        # >1. Obtains temporary OSS upload credentials.
        # >2. Uploads the file stream directly to OSS.
        # >3. Calls the CreateDocParserJob operation with the generated OSS URL.
        self.file_url_object = file_url_object
        self.image_mode = image_mode
        # The OSS file URL.
        self.oss_file_url = oss_file_url
        # The output format of the parsing result. Valid values:
        # 
        # - **markdown**: Markdown format.
        # 
        # This parameter is required.
        self.output_format = output_format
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.result_type = result_type
        self.table_format = table_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.image_mode is not None:
            result['ImageMode'] = self.image_mode

        if self.oss_file_url is not None:
            result['OssFileUrl'] = self.oss_file_url

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.table_format is not None:
            result['TableFormat'] = self.table_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('ImageMode') is not None:
            self.image_mode = m.get('ImageMode')

        if m.get('OssFileUrl') is not None:
            self.oss_file_url = m.get('OssFileUrl')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('TableFormat') is not None:
            self.table_format = m.get('TableFormat')

        return self

