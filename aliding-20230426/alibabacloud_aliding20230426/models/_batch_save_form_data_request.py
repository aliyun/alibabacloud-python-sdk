# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchSaveFormDataRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        asynchronous_execution: bool = None,
        form_data_json_list: List[str] = None,
        form_uuid: str = None,
        keep_running_after_exception: bool = None,
        no_execute_expression: bool = None,
        system_token: str = None,
    ):
        self.app_type = app_type
        self.asynchronous_execution = asynchronous_execution
        self.form_data_json_list = form_data_json_list
        self.form_uuid = form_uuid
        self.keep_running_after_exception = keep_running_after_exception
        self.no_execute_expression = no_execute_expression
        self.system_token = system_token

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

        if self.form_data_json_list is not None:
            result['FormDataJsonList'] = self.form_data_json_list

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.keep_running_after_exception is not None:
            result['KeepRunningAfterException'] = self.keep_running_after_exception

        if self.no_execute_expression is not None:
            result['NoExecuteExpression'] = self.no_execute_expression

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AsynchronousExecution') is not None:
            self.asynchronous_execution = m.get('AsynchronousExecution')

        if m.get('FormDataJsonList') is not None:
            self.form_data_json_list = m.get('FormDataJsonList')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('KeepRunningAfterException') is not None:
            self.keep_running_after_exception = m.get('KeepRunningAfterException')

        if m.get('NoExecuteExpression') is not None:
            self.no_execute_expression = m.get('NoExecuteExpression')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

