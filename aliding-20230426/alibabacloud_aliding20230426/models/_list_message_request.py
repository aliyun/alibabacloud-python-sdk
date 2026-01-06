# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListMessageRequest(DaraModel):
    def __init__(
        self,
        assistant_id: str = None,
        ext_login_user: main_models.ListMessageRequestExtLoginUser = None,
        limit: int = None,
        order: str = None,
        original_assistant_id: str = None,
        run_id: str = None,
        source_id_of_original_assistant_id: str = None,
        source_type_of_original_assistant_id: str = None,
        thread_id: str = None,
    ):
        # This parameter is required.
        self.assistant_id = assistant_id
        self.ext_login_user = ext_login_user
        self.limit = limit
        self.order = order
        self.original_assistant_id = original_assistant_id
        self.run_id = run_id
        self.source_id_of_original_assistant_id = source_id_of_original_assistant_id
        self.source_type_of_original_assistant_id = source_type_of_original_assistant_id
        # This parameter is required.
        self.thread_id = thread_id

    def validate(self):
        if self.ext_login_user:
            self.ext_login_user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant_id is not None:
            result['assistantId'] = self.assistant_id

        if self.ext_login_user is not None:
            result['extLoginUser'] = self.ext_login_user.to_map()

        if self.limit is not None:
            result['limit'] = self.limit

        if self.order is not None:
            result['order'] = self.order

        if self.original_assistant_id is not None:
            result['originalAssistantId'] = self.original_assistant_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.source_id_of_original_assistant_id is not None:
            result['sourceIdOfOriginalAssistantId'] = self.source_id_of_original_assistant_id

        if self.source_type_of_original_assistant_id is not None:
            result['sourceTypeOfOriginalAssistantId'] = self.source_type_of_original_assistant_id

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistantId') is not None:
            self.assistant_id = m.get('assistantId')

        if m.get('extLoginUser') is not None:
            temp_model = main_models.ListMessageRequestExtLoginUser()
            self.ext_login_user = temp_model.from_map(m.get('extLoginUser'))

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('originalAssistantId') is not None:
            self.original_assistant_id = m.get('originalAssistantId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('sourceIdOfOriginalAssistantId') is not None:
            self.source_id_of_original_assistant_id = m.get('sourceIdOfOriginalAssistantId')

        if m.get('sourceTypeOfOriginalAssistantId') is not None:
            self.source_type_of_original_assistant_id = m.get('sourceTypeOfOriginalAssistantId')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

class ListMessageRequestExtLoginUser(DaraModel):
    def __init__(
        self,
        ext_login_user_domain: str = None,
        ext_login_user_id: str = None,
        ext_login_user_name: str = None,
    ):
        self.ext_login_user_domain = ext_login_user_domain
        self.ext_login_user_id = ext_login_user_id
        self.ext_login_user_name = ext_login_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_login_user_domain is not None:
            result['extLoginUserDomain'] = self.ext_login_user_domain

        if self.ext_login_user_id is not None:
            result['extLoginUserId'] = self.ext_login_user_id

        if self.ext_login_user_name is not None:
            result['extLoginUserName'] = self.ext_login_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extLoginUserDomain') is not None:
            self.ext_login_user_domain = m.get('extLoginUserDomain')

        if m.get('extLoginUserId') is not None:
            self.ext_login_user_id = m.get('extLoginUserId')

        if m.get('extLoginUserName') is not None:
            self.ext_login_user_name = m.get('extLoginUserName')

        return self

