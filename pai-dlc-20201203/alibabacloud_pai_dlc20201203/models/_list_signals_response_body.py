# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ListSignalsResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        signals: List[main_models.ListSignalsResponseBodySignals] = None,
        total_count: int = None,
    ):
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.signals = signals
        self.total_count = total_count

    def validate(self):
        if self.signals:
            for v1 in self.signals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Signals'] = []
        if self.signals is not None:
            for k1 in self.signals:
                result['Signals'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.signals = []
        if m.get('Signals') is not None:
            for k1 in m.get('Signals'):
                temp_model = main_models.ListSignalsResponseBodySignals()
                self.signals.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSignalsResponseBodySignals(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        message: str = None,
        pod_names: List[str] = None,
        reason: str = None,
        roles: List[str] = None,
        scope: str = None,
        signal: str = None,
        signal_id: str = None,
        status: str = None,
    ):
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.message = message
        self.pod_names = pod_names
        self.reason = reason
        self.roles = roles
        self.scope = scope
        self.signal = signal
        self.signal_id = signal_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.message is not None:
            result['Message'] = self.message

        if self.pod_names is not None:
            result['PodNames'] = self.pod_names

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.signal is not None:
            result['Signal'] = self.signal

        if self.signal_id is not None:
            result['SignalId'] = self.signal_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PodNames') is not None:
            self.pod_names = m.get('PodNames')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Signal') is not None:
            self.signal = m.get('Signal')

        if m.get('SignalId') is not None:
            self.signal_id = m.get('SignalId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

