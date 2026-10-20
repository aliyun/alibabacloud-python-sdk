# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyFileUploadLeaseRequest(DaraModel):
    def __init__(
        self,
        category_type: str = None,
        file_name: str = None,
        md_5: str = None,
        size_in_bytes: str = None,
        use_internal_endpoint: bool = None,
    ):
        # The category type. If this parameter is not specified, the default value is UNSTRUCTURED. Valid values:
        # 
        # UNSTRUCTURED: category, used for building [knowledge base](https://help.aliyun.com/document_detail/2807740.html) scenarios.
        # <props="china">
        # SESSION_FILE: upload a file for agent application [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction).
        # 
        # 
        # > To create a new data table and upload data, use the Alibaba Cloud Model Studio console. This is not supported through the API.
        # >
        self.category_type = category_type
        # When uploading a file for building a [knowledge base](https://help.aliyun.com/document_detail/2807740.html):
        # - This parameter specifies the name of the file to upload. The file name extension must match the file format. Supported formats:
        #      - Documents (less than 150 MB): doc, docx, wps, ppt, pptx, xls, xlsx, md, txt, pdf, epub, mobi.
        #      - Spreadsheets (10 MB or less recommended, 100,000 rows or less): xls, xlsx.
        #      - Plain text (10 MB or less recommended): md, txt.
        #      - Images (less than 20 MB, shortest side > 15 px, longest side < 8192 px, aspect ratio < 50): png, jpg, jpeg, bmp, gif.
        #      - Audio: aac, amr, flac, flv, m4a, mp3, mpeg, ogg, opus, wav, webm, wma.
        #      - Video: mp4, mkv, avi, mov, wmv.
        # - The file name must be 4 to 128 characters in length. For other limits, see [Knowledge base quotas and limits](https://help.aliyun.com/document_detail/2880605.html).
        # > To create a new data table and upload data, use the Alibaba Cloud Model Studio console. This is not supported through the API.
        # >
        # <props="china">
        # When uploading a file for agent application [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction):
        # 
        # - This parameter specifies the name of the file to upload. The file name extension must match the file format. Supported formats:
        #      - Documents: doc, docx, wps, ppt, pptx, xls, xlsx, md, txt, pdf, epub, mobi.
        #      - Images: png, jpg, jpeg, bmp, gif.
        #      - Audio: aac, amr, flac, flv, m4a, mp3, mpeg, ogg, opus, wav, webm, wma.
        #      - Video: mp4, mkv, avi, mov, wmv.
        # - The file name must be 4 to 128 characters in length.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The MD5 value of the file to upload. The server validates this parameter (validation is not currently enabled). Specify the correct value.
        # 
        # This parameter is required.
        self.md_5 = md_5
        # The size of the file to upload, in bytes. The server validates this parameter (validation is not currently enabled). Specify the correct value. Valid values: 1 B to 100 MB.
        # 
        # This parameter is required.
        self.size_in_bytes = size_in_bytes
        # <props="china">
        # 
        # If you use [Alibaba Cloud Model Studio secure storage](https://www.alibabacloud.com/help/en/model-studio/configure-resources-in-private-network) and need to generate a lease URL accessible only from the Alibaba Cloud internal network in the same region, set this parameter to true for improved security. If this parameter is not specified, the default value is false, which generates a publicly accessible lease URL.
        # > If you have not activated Alibaba Cloud Model Studio secure storage, or are unsure whether you are using it, do not set this parameter to true (the upload will fail).
        # 
        # 
        # 
        # <props="intl">
        # 
        # If you use Alibaba Cloud Model Studio secure storage and need to generate a lease URL accessible only from the Alibaba Cloud internal network in the same region, set this parameter to true for improved security. If this parameter is not specified, the default value is false, which generates a publicly accessible lease URL.
        # > If you have not activated Alibaba Cloud Model Studio secure storage, or are unsure whether you are using it, do not set this parameter to true (the upload will fail).
        self.use_internal_endpoint = use_internal_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.size_in_bytes is not None:
            result['SizeInBytes'] = self.size_in_bytes

        if self.use_internal_endpoint is not None:
            result['UseInternalEndpoint'] = self.use_internal_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('SizeInBytes') is not None:
            self.size_in_bytes = m.get('SizeInBytes')

        if m.get('UseInternalEndpoint') is not None:
            self.use_internal_endpoint = m.get('UseInternalEndpoint')

        return self

