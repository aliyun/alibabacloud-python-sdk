# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFileShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        category_type: str = None,
        lease_id: str = None,
        original_file_url: str = None,
        parser: str = None,
        parser_config_shrink: str = None,
        tags_shrink: str = None,
    ):
        # <props="china">
        # 
        # - If `CategoryType` is set to `UNSTRUCTURED`, you must specify the ID of the category to which the file belongs. This is the `CategoryId` returned by the **AddCategory** API. You can also obtain the category ID by navigating to the \\*\\*Application data\\*\\* > \\*\\*Files\\*\\* tab and clicking the ID icon next to the category name. You can specify `default` to use the default category.
        # 
        # - If `CategoryType` is set to `SESSION_FILE`, specify `default`.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The ID of the category to which the file belongs. This is the `CategoryId` returned by the **AddCategory** API. You can also obtain the category ID by navigating to the \\*\\*Application data\\*\\* > \\*\\*Files\\*\\* tab and clicking the ID icon next to the category name. You can specify `default` to use the default category.
        # 
        # This parameter is required.
        self.category_id = category_id
        # The type of category. This parameter is optional. Default value: `UNSTRUCTURED`. Valid values:
        # 
        # - `UNSTRUCTURED`: A category used for building a knowledge base.
        # 
        # <props="china">
        # 
        # - `SESSION_FILE`: A file used for interactions within an agent [session](https://help.aliyun.com/zh/model-studio/user-guide/file-interaction).
        #   > If you set this parameter to `SESSION_FILE`, you must also set the `CategoryType` parameter to `SESSION_FILE` when you call the ApplyFileUploadLease API.
        #   > Files of this type are valid only for the current session and expire after the session is closed, with a maximum validity of 7 days. These files are not intended for long-term storage.
        self.category_type = category_type
        # The upload lease ID. This value maps to the `FileUploadLeaseId` returned by the **ApplyFileUploadLease** API.
        # 
        # This parameter is required.
        self.lease_id = lease_id
        # <props="china">
        # 
        # The URL of the file. The system records this link when building a [document retrieval-based knowledge base](https://help.aliyun.com/document_detail/2807740.html). When you interact with an [agent](https://help.aliyun.com/document_detail/2842749.html) in the Alibaba Cloud Model Studio console, this URL is returned with the retrieval results for the file in the `docUrl` field.
        # 
        # > For this parameter to take effect, the **knowledge base** feature must be enabled for the agent, and the **display the source of the answer** option must be enabled.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The URL of the file. The system records this link when building a [document retrieval-based knowledge base](https://help.aliyun.com/document_detail/2807740.html). When you interact with an [agent](https://help.aliyun.com/document_detail/2842749.html) in the Alibaba Cloud Model Studio console, this URL is returned with the retrieval results for the file in the `docUrl` field.
        # 
        # > For this parameter to take effect, the **knowledge base** feature must be enabled for the agent, and the **display the source of the answer** option must be enabled.
        self.original_file_url = original_file_url
        # The type of parser. Valid values:
        # 
        # - DOCMIND: Intelligent Document Parsing
        # 
        # - DOCMIND_DIGITAL: Digital Document Parsing
        # 
        # - DOCMIND_LLM_VERSION: Large Language Model-based Document Parsing
        # 
        # - DASH_QWEN_VL_PARSER: Qwen-VL Parsing
        # 
        # - DOCMIND_LLM_VERSION_MEDIA: Audio and Video Parsing
        # 
        # - AUTO_SELECT: Automatic Parser Selection
        # 
        # <props="intl">
        # 
        # > The system uses the specified parser to parse the uploaded file. If you set this parameter to `AUTO_SELECT`, the parser configured for the category is used.
        # 
        # 
        # 
        # <props="china">
        # 
        # > If `CategoryType` is set to `UNSTRUCTURED`, the parser parses your uploaded file based on the category’s data parsing settings.
        # > If `CategoryType` is set to `SESSION_FILE`, the system uses a default parsing method that cannot be changed.
        # 
        # This parameter is required.
        self.parser = parser
        # The parser configuration. This parameter is required only if you set `Parser` to `DASH_QWEN_VL_PARSER`.
        self.parser_config_shrink = parser_config_shrink
        # - A list of tags for the file. You can specify up to 100 tags. The total length of all tags cannot exceed 700 characters.
        # 
        # - If this parameter is not specified, no tags are added.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

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

        if self.parser_config_shrink is not None:
            result['ParserConfig'] = self.parser_config_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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
            self.parser_config_shrink = m.get('ParserConfig')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

