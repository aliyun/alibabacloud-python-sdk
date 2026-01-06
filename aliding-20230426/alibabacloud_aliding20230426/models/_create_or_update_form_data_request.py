# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateFormDataRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_data_json: str = None,
        form_uuid: str = None,
        no_execute_expression: bool = None,
        search_condition: str = None,
        system_token: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.form_data_json = form_data_json
        self.form_uuid = form_uuid
        self.no_execute_expression = no_execute_expression
        self.search_condition = search_condition
        self.system_token = system_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.form_data_json is not None:
            result['FormDataJson'] = self.form_data_json

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.no_execute_expression is not None:
            result['NoExecuteExpression'] = self.no_execute_expression

        if self.search_condition is not None:
            result['SearchCondition'] = self.search_condition

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormDataJson') is not None:
            self.form_data_json = m.get('FormDataJson')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('NoExecuteExpression') is not None:
            self.no_execute_expression = m.get('NoExecuteExpression')

        if m.get('SearchCondition') is not None:
            self.search_condition = m.get('SearchCondition')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

