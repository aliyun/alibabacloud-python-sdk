# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetQuotaUtilizationOverviewResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        generated_at: str = None,
        message: str = None,
        quota_overview: main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverview = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.generated_at = generated_at
        self.message = message
        self.quota_overview = quota_overview
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.quota_overview:
            self.quota_overview.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.generated_at is not None:
            result['GeneratedAt'] = self.generated_at

        if self.message is not None:
            result['Message'] = self.message

        if self.quota_overview is not None:
            result['QuotaOverview'] = self.quota_overview.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GeneratedAt') is not None:
            self.generated_at = m.get('GeneratedAt')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QuotaOverview') is not None:
            temp_model = main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverview()
            self.quota_overview = temp_model.from_map(m.get('QuotaOverview'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQuotaUtilizationOverviewResponseBodyQuotaOverview(DaraModel):
    def __init__(
        self,
        in_use: main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewInUse = None,
        over_80percent: main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver80Percent = None,
        over_95percent: main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver95Percent = None,
    ):
        self.in_use = in_use
        self.over_80percent = over_80percent
        self.over_95percent = over_95percent

    def validate(self):
        if self.in_use:
            self.in_use.validate()
        if self.over_80percent:
            self.over_80percent.validate()
        if self.over_95percent:
            self.over_95percent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_use is not None:
            result['InUse'] = self.in_use.to_map()

        if self.over_80percent is not None:
            result['Over80Percent'] = self.over_80percent.to_map()

        if self.over_95percent is not None:
            result['Over95Percent'] = self.over_95percent.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InUse') is not None:
            temp_model = main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewInUse()
            self.in_use = temp_model.from_map(m.get('InUse'))

        if m.get('Over80Percent') is not None:
            temp_model = main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver80Percent()
            self.over_80percent = temp_model.from_map(m.get('Over80Percent'))

        if m.get('Over95Percent') is not None:
            temp_model = main_models.GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver95Percent()
            self.over_95percent = temp_model.from_map(m.get('Over95Percent'))

        return self

class GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver95Percent(DaraModel):
    def __init__(
        self,
        adjustable: int = None,
        adjustable_ratio: float = None,
        total: int = None,
    ):
        self.adjustable = adjustable
        self.adjustable_ratio = adjustable_ratio
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.adjustable_ratio is not None:
            result['AdjustableRatio'] = self.adjustable_ratio

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('AdjustableRatio') is not None:
            self.adjustable_ratio = m.get('AdjustableRatio')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQuotaUtilizationOverviewResponseBodyQuotaOverviewOver80Percent(DaraModel):
    def __init__(
        self,
        adjustable: int = None,
        adjustable_ratio: float = None,
        total: int = None,
    ):
        self.adjustable = adjustable
        self.adjustable_ratio = adjustable_ratio
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.adjustable_ratio is not None:
            result['AdjustableRatio'] = self.adjustable_ratio

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('AdjustableRatio') is not None:
            self.adjustable_ratio = m.get('AdjustableRatio')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQuotaUtilizationOverviewResponseBodyQuotaOverviewInUse(DaraModel):
    def __init__(
        self,
        adjustable: int = None,
        adjustable_ratio: float = None,
        total: int = None,
    ):
        self.adjustable = adjustable
        self.adjustable_ratio = adjustable_ratio
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable

        if self.adjustable_ratio is not None:
            result['AdjustableRatio'] = self.adjustable_ratio

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')

        if m.get('AdjustableRatio') is not None:
            self.adjustable_ratio = m.get('AdjustableRatio')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

