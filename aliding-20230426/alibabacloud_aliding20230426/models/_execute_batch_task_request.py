# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteBatchTaskRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        out_result: str = None,
        remark: str = None,
        system_token: str = None,
        task_information_list: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.out_result = out_result
        self.remark = remark
        # This parameter is required.
        self.system_token = system_token
        # This parameter is required.
        self.task_information_list = task_information_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.out_result is not None:
            result['OutResult'] = self.out_result

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.task_information_list is not None:
            result['TaskInformationList'] = self.task_information_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('OutResult') is not None:
            self.out_result = m.get('OutResult')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TaskInformationList') is not None:
            self.task_information_list = m.get('TaskInformationList')

        return self

