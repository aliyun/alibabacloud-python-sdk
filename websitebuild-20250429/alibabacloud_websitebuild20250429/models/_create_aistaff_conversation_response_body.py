# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CreateAIStaffConversationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.CreateAIStaffConversationResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access was denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name. The application with this name is queried.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message.
        self.dynamic_message = dynamic_message
        # The error parameters returned.
        self.error_args = error_args
        # The response data.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The exception message.
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
            temp_model = main_models.CreateAIStaffConversationResponseBodyModule()
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

class CreateAIStaffConversationResponseBodyModule(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        chat_id: str = None,
        conversation_id: str = None,
        section_id: str = None,
        site_id: str = None,
        title: str = None,
    ):
        # The chatbot ID.
        self.bot_id = bot_id
        # The chat ID.
        self.chat_id = chat_id
        # The session ID.
        self.conversation_id = conversation_id
        # The section ID of the check item.
        self.section_id = section_id
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        self.site_id = site_id
        # The current viewpoint, equivalent to the news title.
        self.title = title

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

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

