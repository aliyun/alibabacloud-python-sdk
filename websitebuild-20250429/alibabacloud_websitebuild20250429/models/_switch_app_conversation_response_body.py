# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class SwitchAppConversationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.SwitchAppConversationResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
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
            temp_model = main_models.SwitchAppConversationResponseBodyModule()
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

class SwitchAppConversationResponseBodyModule(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        bot_id: str = None,
        chat_num: int = None,
        conversation_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        meta_data: str = None,
        section_id: str = None,
        site_id: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.aliyun_pk = aliyun_pk
        self.bot_id = bot_id
        self.chat_num = chat_num
        self.conversation_id = conversation_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.meta_data = meta_data
        self.section_id = section_id
        self.site_id = site_id
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['AliyunPk'] = self.aliyun_pk

        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.chat_num is not None:
            result['ChatNum'] = self.chat_num

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunPk') is not None:
            self.aliyun_pk = m.get('AliyunPk')

        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('ChatNum') is not None:
            self.chat_num = m.get('ChatNum')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

