# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTaskRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        digital_sign_url: str = None,
        form_data_json: str = None,
        language: str = None,
        no_execute_expressions: str = None,
        out_result: str = None,
        process_instance_id: str = None,
        remark: str = None,
        system_token: str = None,
        task_id: int = None,
    ):
        self.app_type = app_type
        self.digital_sign_url = digital_sign_url
        self.form_data_json = form_data_json
        self.language = language
        self.no_execute_expressions = no_execute_expressions
        self.out_result = out_result
        self.process_instance_id = process_instance_id
        self.remark = remark
        self.system_token = system_token
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.digital_sign_url is not None:
            result['DigitalSignUrl'] = self.digital_sign_url

        if self.form_data_json is not None:
            result['FormDataJson'] = self.form_data_json

        if self.language is not None:
            result['Language'] = self.language

        if self.no_execute_expressions is not None:
            result['NoExecuteExpressions'] = self.no_execute_expressions

        if self.out_result is not None:
            result['OutResult'] = self.out_result

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('DigitalSignUrl') is not None:
            self.digital_sign_url = m.get('DigitalSignUrl')

        if m.get('FormDataJson') is not None:
            self.form_data_json = m.get('FormDataJson')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NoExecuteExpressions') is not None:
            self.no_execute_expressions = m.get('NoExecuteExpressions')

        if m.get('OutResult') is not None:
            self.out_result = m.get('OutResult')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

