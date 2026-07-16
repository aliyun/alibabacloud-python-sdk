# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddFileRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        lease_id: str = None,
        original_file_url: str = None,
        parser: str = None,
        parser_config: main_models.AddFileRequestParserConfig = None,
        tags: List[str] = None,
    ):
        # <props="china">
        # 
        # - When CategoryType is set to UNSTRUCTURED, set this parameter to the category ID of the uploaded file, which is the `CategoryId` returned by the **AddCategory** operation. You can also go to [Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center), click the File tab, and then click the ID icon next to the category name to obtain the category ID. You can set this parameter to default to use the system-created default category.
        # 
        # - When CategoryType is set to SESSION_FILE, set this parameter to "default".
        # 
        # 
        # <props="intl">
        # 
        # Set this parameter to the category ID of the uploaded file, which is the `CategoryId` returned by the **AddCategory** operation. You can also go to [Application Data](https://modelstudio.console.alibabacloud.com/?tab=app#/data-center), click the File tab, and then click the ID icon next to the category name to obtain the category ID. You can set this parameter to default to use the system-created default category.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The category type. This parameter is optional. Default value: UNSTRUCTURED. Valid values:
        # - UNSTRUCTURED: category used for building knowledge base scenarios.
        # 
        # <props="china">
        # - SESSION_FILE: file used for [session interaction](https://www.alibabacloud.com/help/en/model-studio/user-guide/file-interaction) in agent applications.
        # <note>When using `SESSION_FILE`, set the CategoryType parameter to `SESSION_FILE` when calling the ApplyFileUploadLease operation as well.</note>
        # <note>The file is valid only for the current user session. After the user closes the session, the file expires. The maximum validity period is 7 days. Long-term storage is not supported.</note>
        self.category_type = category_type
        # The upload lease ID, which corresponds to the `FileUploadLeaseId` returned by the **ApplyFileUploadLease** operation.
        # 
        # This parameter is required.
        self.lease_id = lease_id
        # <props="china">
        # 
        # Specifies a URL for the file. The system records this URL when building a [document search knowledge base](https://help.aliyun.com/document_detail/2807740.html). When you use the Alibaba Cloud Model Studio console to interact with an [agent application](https://help.aliyun.com/document_detail/2842749.html), this URL is returned with the retrieval results of the file through the `docUrl` field.
        # 
        # > The agent application must have **Knowledge Base** enabled and the **Show answer sources** feature turned on. Otherwise, this parameter does not take effect.
        # 
        # 
        # 
        # <props="intl">
        # 
        # Specifies a URL for the file. The system records this URL when building a [document search knowledge base](https://help.aliyun.com/document_detail/2807740.html). When you use the Alibaba Cloud Model Studio console to interact with an [agent application](https://help.aliyun.com/document_detail/2842749.html), this URL is returned with the retrieval results of the file through the `docUrl` field.
        # 
        # > The agent application must have **Knowledge Base** enabled and the **Show answer sources** feature turned on. Otherwise, this parameter does not take effect.
        self.original_file_url = original_file_url
        # The parser type. Valid values:
        # 
        # - DOCMIND: intelligent document parsing
        # - DOCMIND_DIGITAL: electronic document parsing
        # - DOCMIND_LLM_VERSION: large language model document parsing
        # - DASH_QWEN_VL_PARSER: Qwen VL parsing
        # - DOCMIND_LLM_VERSION_MEDIA: audio and video parsing
        # - AUTO_SELECT: automatic parser selection
        # 
        # <props="intl">
        # <note>The uploaded file is parsed by using the currently specified parser. If you set this parameter to AUTO_SELECT, the parser configured for the category is used.</note>
        # 
        # 
        # <props="china">
        # <note>When CategoryType is set to UNSTRUCTURED, the parser parses the uploaded file based on the data parsing settings of the current category.</note>
        # <note>When CategoryType is set to SESSION_FILE, the system parses the file content by using the default method, which cannot be changed.</note>
        # 
        # This parameter is required.
        self.parser = parser
        # The parser configuration. This parameter is required only when the parser type is set to Qwen VL parsing.
        self.parser_config = parser_config
        # - The list of tags associated with the file. You can specify up to 100 tags, and the total character length of all tags cannot exceed 700.
        # - Default value: empty, which means no tags are set.
        self.tags = tags

    def validate(self):
        if self.parser_config:
            self.parser_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.lease_id is not None:
            result['LeaseId'] = self.lease_id

        if self.original_file_url is not None:
            result['OriginalFileUrl'] = self.original_file_url

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.parser_config is not None:
            result['ParserConfig'] = self.parser_config.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('LeaseId') is not None:
            self.lease_id = m.get('LeaseId')

        if m.get('OriginalFileUrl') is not None:
            self.original_file_url = m.get('OriginalFileUrl')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('ParserConfig') is not None:
            temp_model = main_models.AddFileRequestParserConfig()
            self.parser_config = temp_model.from_map(m.get('ParserConfig'))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class AddFileRequestParserConfig(DaraModel):
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

