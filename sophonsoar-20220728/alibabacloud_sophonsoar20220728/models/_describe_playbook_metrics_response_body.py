# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metrics: main_models.DescribePlaybookMetricsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        # The details of the playbook.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.DescribePlaybookMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookMetricsResponseBodyMetrics(DaraModel):
    def __init__(
        self,
        active: int = None,
        description: str = None,
        display_name: str = None,
        fail_num: int = None,
        gmt_create: int = None,
        history_md_5: int = None,
        last_runtime: int = None,
        own_type: str = None,
        playbook_uuid: str = None,
        succ_num: int = None,
    ):
        # The status of the playbook. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.active = active
        # The description of the playbook.
        self.description = description
        # The name of the playbook.
        self.display_name = display_name
        # The number of the tasks that are created for the playbook and failed to run.
        self.fail_num = fail_num
        # The time when the playbook was created. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The number of historical versions of the playbook.
        self.history_md_5 = history_md_5
        # The time when the playbook was last run. The value is a 13-digit timestamp.
        self.last_runtime = last_runtime
        # The type of the playbook. Valid values:
        # 
        # *   **preset**: predefined playbook
        # *   **user**: custom playbook
        self.own_type = own_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The number of the tasks that are created for the playbook and were successfully run.
        self.succ_num = succ_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.fail_num is not None:
            result['FailNum'] = self.fail_num

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.history_md_5 is not None:
            result['HistoryMd5'] = self.history_md_5

        if self.last_runtime is not None:
            result['LastRuntime'] = self.last_runtime

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.succ_num is not None:
            result['SuccNum'] = self.succ_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('HistoryMd5') is not None:
            self.history_md_5 = m.get('HistoryMd5')

        if m.get('LastRuntime') is not None:
            self.last_runtime = m.get('LastRuntime')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('SuccNum') is not None:
            self.succ_num = m.get('SuccNum')

        return self

