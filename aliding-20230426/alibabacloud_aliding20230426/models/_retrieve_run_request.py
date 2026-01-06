# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class RetrieveRunRequest(DaraModel):
    def __init__(
        self,
        assistant_id: str = None,
        ext_login_user: main_models.RetrieveRunRequestExtLoginUser = None,
        original_assistant_id: str = None,
        run_id: str = None,
        source_id_of_original_assistant_id: str = None,
        source_type_of_original_assistant_id: str = None,
    ):
        # This parameter is required.
        self.assistant_id = assistant_id
        self.ext_login_user = ext_login_user
        self.original_assistant_id = original_assistant_id
        self.run_id = run_id
        self.source_id_of_original_assistant_id = source_id_of_original_assistant_id
        self.source_type_of_original_assistant_id = source_type_of_original_assistant_id

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

        if self.original_assistant_id is not None:
            result['originalAssistantId'] = self.original_assistant_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.source_id_of_original_assistant_id is not None:
            result['sourceIdOfOriginalAssistantId'] = self.source_id_of_original_assistant_id

        if self.source_type_of_original_assistant_id is not None:
            result['sourceTypeOfOriginalAssistantId'] = self.source_type_of_original_assistant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistantId') is not None:
            self.assistant_id = m.get('assistantId')

        if m.get('extLoginUser') is not None:
            temp_model = main_models.RetrieveRunRequestExtLoginUser()
            self.ext_login_user = temp_model.from_map(m.get('extLoginUser'))

        if m.get('originalAssistantId') is not None:
            self.original_assistant_id = m.get('originalAssistantId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('sourceIdOfOriginalAssistantId') is not None:
            self.source_id_of_original_assistant_id = m.get('sourceIdOfOriginalAssistantId')

        if m.get('sourceTypeOfOriginalAssistantId') is not None:
            self.source_type_of_original_assistant_id = m.get('sourceTypeOfOriginalAssistantId')

        return self

class RetrieveRunRequestExtLoginUser(DaraModel):
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

