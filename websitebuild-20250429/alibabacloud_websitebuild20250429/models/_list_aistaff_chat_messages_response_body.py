# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAIStaffChatMessagesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.ListAIStaffChatMessagesResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The access denied details.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not in use. Ignore it.
        self.dynamic_message = dynamic_message
        # The error parameters.
        self.error_args = error_args
        # The response data.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The error message.
        self.root_error_msg = root_error_msg
        # The reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.ListAIStaffChatMessagesResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAIStaffChatMessagesResponseBodyModule(DaraModel):
    def __init__(
        self,
        messages: List[main_models.ListAIStaffChatMessagesResponseBodyModuleMessages] = None,
    ):
        # The sender type.
        # 
        # Valid values:
        # - **ADMIN**: System.
        # - **CUSTOMER**: Visitor.
        # - **AGENT**: Agent.
        self.messages = messages

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.ListAIStaffChatMessagesResponseBodyModuleMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class ListAIStaffChatMessagesResponseBodyModuleMessages(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        chat_id: str = None,
        chat_status: str = None,
        content: str = None,
        content_type: str = None,
        conversation_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        meta_data: Dict[str, Any] = None,
        role: str = None,
        section_id: str = None,
        site_id: str = None,
        type: str = None,
    ):
        # The bot ID.
        self.bot_id = bot_id
        # The ID of the current conversation turn.
        self.chat_id = chat_id
        # The current conversation status.
        self.chat_status = chat_status
        # The ID of the data API operation that is called.
        self.content = content
        # The content type.
        self.content_type = content_type
        # The conversation ID.
        self.conversation_id = conversation_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The message ID.
        self.message_id = message_id
        # The business extension metadata in Map format. The value must be a JSON string.
        self.meta_data = meta_data
        # The role of the conversation participant. Valid values:
        # 
        # - user: User.
        # 
        # - assistant: Assistant.
        # 
        # - system: System.
        # - function: Function.
        # 
        # - plugin: Plugin.
        # 
        # - tool: Tool.
        self.role = role
        # The section ID of the check item.
        self.section_id = section_id
        # The site ID.
        self.site_id = site_id
        # The file type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.chat_status is not None:
            result['ChatStatus'] = self.chat_status

        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.role is not None:
            result['Role'] = self.role

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ChatStatus') is not None:
            self.chat_status = m.get('ChatStatus')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

