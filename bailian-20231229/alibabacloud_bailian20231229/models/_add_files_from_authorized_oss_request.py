# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddFilesFromAuthorizedOssRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        file_details: List[main_models.AddFilesFromAuthorizedOssRequestFileDetails] = None,
        oss_bucket_name: str = None,
        oss_region_id: str = None,
        over_write_file_by_oss_key: bool = None,
        tags: List[str] = None,
    ):
        # The ID of the destination category for the imported files. This is the CategoryId returned by the AddCategory operation. You can also obtain the category ID by clicking the ID icon next to the category name on the <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) > Files tab<props="intl">[Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center) > Files tab. You can set this parameter to default to use the default category created by the system.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The category type. This parameter is optional. Default value: UNSTRUCTURED. Valid values:
        # - UNSTRUCTURED: category, used for building knowledge bases.
        # 
        # <props="china">
        # 
        # > This operation does not support importing SESSION_FILE for [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction) in agent applications. Use the **AddFile** operation to upload SESSION_FILE from your local machine.
        # 
        # This parameter is required.
        self.category_type = category_type
        # The list of files to import. You can upload up to 10 files at a time.
        # > You can upload up to 10 files at a time.
        # >
        # 
        # This parameter is required.
        self.file_details = file_details
        # The name of the OSS bucket. For more information, see [Buckets](https://help.aliyun.com/document_detail/177682.html). Before you import data from OSS for the first time, you must complete the authorization as prompted in the Model Studio console and add a tag with the key bailian-datahub-access and the value read to the destination bucket. You must also authorize the OSS service-linked role as prompted in the Model Studio console (service name: datahub.sfm.aliyuncs.com).
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # The region ID of the OSS bucket. For more information about how to obtain the ID, see [OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html).
        # 
        # This parameter is required.
        self.oss_region_id = oss_region_id
        # Specifies whether to overwrite identical files in the category based on the OssKey. Default value: false, which means identical files are not overwritten.
        self.over_write_file_by_oss_key = over_write_file_by_oss_key
        # The list of tags associated with the file. Default value: empty, which means the file is not associated with any tags. You can specify up to 10 tags.
        self.tags = tags

    def validate(self):
        if self.file_details:
            for v1 in self.file_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        result['FileDetails'] = []
        if self.file_details is not None:
            for k1 in self.file_details:
                result['FileDetails'].append(k1.to_map() if k1 else None)

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id

        if self.over_write_file_by_oss_key is not None:
            result['OverWriteFileByOssKey'] = self.over_write_file_by_oss_key

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        self.file_details = []
        if m.get('FileDetails') is not None:
            for k1 in m.get('FileDetails'):
                temp_model = main_models.AddFilesFromAuthorizedOssRequestFileDetails()
                self.file_details.append(temp_model.from_map(k1))

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')

        if m.get('OverWriteFileByOssKey') is not None:
            self.over_write_file_by_oss_key = m.get('OverWriteFileByOssKey')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class AddFilesFromAuthorizedOssRequestFileDetails(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        oss_key: str = None,
        parser: str = None,
        parser_config: main_models.AddFilesFromAuthorizedOssRequestFileDetailsParserConfig = None,
    ):
        # The name of the file to import. Make sure that the file name extension is included.
        # - Supported formats: pdf, docx, doc, txt, md, pptx, ppt, xlsx, xls, html, png, jpg, jpeg, bmp, and gif.
        # - The file name must be 4 to 128 characters in length.
        # - For more information about the limits on file uploads, see [Knowledge base quotas and limits](https://help.aliyun.com/document_detail/2880605.html).
        # 
        # >Notice: If the name of the imported file is the same as the name of an existing file in the knowledge base, the operation still returns SUCCESS for Status, but the file is not actually imported into the knowledge base and the existing file with the same name remains unchanged. Make sure that the name of each imported file is unique.</notice>
        # > To add a data table and upload data, use the Alibaba Cloud Model Studio console. This is not supported by the API.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The key of the imported file in the OSS bucket. For more information, see [Object naming](https://help.aliyun.com/document_detail/273129.html).
        # 
        # This parameter is required.
        self.oss_key = oss_key
        # The parser type. Valid values:
        # 
        # - DOCMIND (Intelligent document parsing)
        # - DOCMIND_DIGITAL (Electronic document parsing)
        # - DOCMIND_LLM_VERSION (Large model document parsing)
        # - DASH_QWEN_VL_PARSER (Qwen VL parsing)
        # - DOCMIND_LLM_VERSION_MEDIA (Audio and video parsing)
        # - AUTO_SELECT (Automatic parser selection)
        # 
        # <props="intl">
        # <note>The uploaded file is parsed by using the specified parser. If you set this parameter to AUTO_SELECT, the parser configured for the category is used.</note>
        # 
        # 
        # <props="china">
        # <note>If CategoryType is set to UNSTRUCTURED, the file is parsed based on the data parsing settings of the current category.</note>
        # <note>If CategoryType is set to SESSION_FILE, the system parses the file content by using the default method, which cannot be changed.</note>
        self.parser = parser
        # The parser configuration. This parameter is required only when the parser type is set to Qwen VL parsing.
        self.parser_config = parser_config

    def validate(self):
        if self.parser_config:
            self.parser_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.parser_config is not None:
            result['ParserConfig'] = self.parser_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('ParserConfig') is not None:
            temp_model = main_models.AddFilesFromAuthorizedOssRequestFileDetailsParserConfig()
            self.parser_config = temp_model.from_map(m.get('ParserConfig'))

        return self

class AddFilesFromAuthorizedOssRequestFileDetailsParserConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_prompt: str = None,
    ):
        # The model name.
        self.model_name = model_name
        # The prompt used when calling Qwen VL parsing.
        self.model_prompt = model_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_prompt is not None:
            result['ModelPrompt'] = self.model_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelPrompt') is not None:
            self.model_prompt = m.get('ModelPrompt')

        return self

