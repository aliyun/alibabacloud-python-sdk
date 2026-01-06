# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateFormDataByInstanceIdShrinkRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        asynchronous_execution: bool = None,
        form_instance_id_list_shrink: str = None,
        form_uuid: str = None,
        ignore_empty: bool = None,
        no_execute_expression: bool = None,
        system_token: str = None,
        update_form_data_json: str = None,
        use_latest_form_schema_version: bool = None,
    ):
        self.app_type = app_type
        self.asynchronous_execution = asynchronous_execution
        # This parameter is required.
        self.form_instance_id_list_shrink = form_instance_id_list_shrink
        # This parameter is required.
        self.form_uuid = form_uuid
        self.ignore_empty = ignore_empty
        self.no_execute_expression = no_execute_expression
        # This parameter is required.
        self.system_token = system_token
        # This parameter is required.
        self.update_form_data_json = update_form_data_json
        self.use_latest_form_schema_version = use_latest_form_schema_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.asynchronous_execution is not None:
            result['AsynchronousExecution'] = self.asynchronous_execution

        if self.form_instance_id_list_shrink is not None:
            result['FormInstanceIdList'] = self.form_instance_id_list_shrink

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.ignore_empty is not None:
            result['IgnoreEmpty'] = self.ignore_empty

        if self.no_execute_expression is not None:
            result['NoExecuteExpression'] = self.no_execute_expression

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.update_form_data_json is not None:
            result['UpdateFormDataJson'] = self.update_form_data_json

        if self.use_latest_form_schema_version is not None:
            result['UseLatestFormSchemaVersion'] = self.use_latest_form_schema_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AsynchronousExecution') is not None:
            self.asynchronous_execution = m.get('AsynchronousExecution')

        if m.get('FormInstanceIdList') is not None:
            self.form_instance_id_list_shrink = m.get('FormInstanceIdList')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('IgnoreEmpty') is not None:
            self.ignore_empty = m.get('IgnoreEmpty')

        if m.get('NoExecuteExpression') is not None:
            self.no_execute_expression = m.get('NoExecuteExpression')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('UpdateFormDataJson') is not None:
            self.update_form_data_json = m.get('UpdateFormDataJson')

        if m.get('UseLatestFormSchemaVersion') is not None:
            self.use_latest_form_schema_version = m.get('UseLatestFormSchemaVersion')

        return self

