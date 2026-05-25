# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class GetIssueResponseBody(DaraModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: main_models.GetIssueResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.GetIssueResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetIssueResponseBodyModel(DaraModel):
    def __init__(
        self,
        affected_versions: List[str] = None,
        alloc_size_max: int = None,
        alloc_size_pct_50: int = None,
        alloc_size_pct_70: int = None,
        alloc_size_pct_90: int = None,
        crux_stack: str = None,
        digest_hash: str = None,
        error_column: int = None,
        error_count: int = None,
        error_count_growth_rate: float = None,
        error_device_count: int = None,
        error_device_count_growth_rate: float = None,
        error_device_rate: float = None,
        error_device_rate_growth_rate: float = None,
        error_file_name: str = None,
        error_line: str = None,
        error_name: str = None,
        error_rate: float = None,
        error_rate_growth_rate: float = None,
        error_type: str = None,
        event_time: int = None,
        first_version: str = None,
        gmt_create: int = None,
        gmt_latest: int = None,
        key_line: int = None,
        name: str = None,
        reason: str = None,
        stack: str = None,
        status: int = None,
        summary: str = None,
        symbolic_status: bool = None,
        tags: List[str] = None,
        type: str = None,
    ):
        self.affected_versions = affected_versions
        self.alloc_size_max = alloc_size_max
        self.alloc_size_pct_50 = alloc_size_pct_50
        self.alloc_size_pct_70 = alloc_size_pct_70
        self.alloc_size_pct_90 = alloc_size_pct_90
        self.crux_stack = crux_stack
        self.digest_hash = digest_hash
        self.error_column = error_column
        self.error_count = error_count
        self.error_count_growth_rate = error_count_growth_rate
        self.error_device_count = error_device_count
        self.error_device_count_growth_rate = error_device_count_growth_rate
        self.error_device_rate = error_device_rate
        self.error_device_rate_growth_rate = error_device_rate_growth_rate
        self.error_file_name = error_file_name
        self.error_line = error_line
        self.error_name = error_name
        self.error_rate = error_rate
        self.error_rate_growth_rate = error_rate_growth_rate
        self.error_type = error_type
        self.event_time = event_time
        self.first_version = first_version
        self.gmt_create = gmt_create
        self.gmt_latest = gmt_latest
        self.key_line = key_line
        self.name = name
        self.reason = reason
        self.stack = stack
        self.status = status
        self.summary = summary
        self.symbolic_status = symbolic_status
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_versions is not None:
            result['AffectedVersions'] = self.affected_versions

        if self.alloc_size_max is not None:
            result['AllocSizeMax'] = self.alloc_size_max

        if self.alloc_size_pct_50 is not None:
            result['AllocSizePct50'] = self.alloc_size_pct_50

        if self.alloc_size_pct_70 is not None:
            result['AllocSizePct70'] = self.alloc_size_pct_70

        if self.alloc_size_pct_90 is not None:
            result['AllocSizePct90'] = self.alloc_size_pct_90

        if self.crux_stack is not None:
            result['CruxStack'] = self.crux_stack

        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash

        if self.error_column is not None:
            result['ErrorColumn'] = self.error_column

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.error_count_growth_rate is not None:
            result['ErrorCountGrowthRate'] = self.error_count_growth_rate

        if self.error_device_count is not None:
            result['ErrorDeviceCount'] = self.error_device_count

        if self.error_device_count_growth_rate is not None:
            result['ErrorDeviceCountGrowthRate'] = self.error_device_count_growth_rate

        if self.error_device_rate is not None:
            result['ErrorDeviceRate'] = self.error_device_rate

        if self.error_device_rate_growth_rate is not None:
            result['ErrorDeviceRateGrowthRate'] = self.error_device_rate_growth_rate

        if self.error_file_name is not None:
            result['ErrorFileName'] = self.error_file_name

        if self.error_line is not None:
            result['ErrorLine'] = self.error_line

        if self.error_name is not None:
            result['ErrorName'] = self.error_name

        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate

        if self.error_rate_growth_rate is not None:
            result['ErrorRateGrowthRate'] = self.error_rate_growth_rate

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.first_version is not None:
            result['FirstVersion'] = self.first_version

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_latest is not None:
            result['GmtLatest'] = self.gmt_latest

        if self.key_line is not None:
            result['KeyLine'] = self.key_line

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.stack is not None:
            result['Stack'] = self.stack

        if self.status is not None:
            result['Status'] = self.status

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.symbolic_status is not None:
            result['SymbolicStatus'] = self.symbolic_status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedVersions') is not None:
            self.affected_versions = m.get('AffectedVersions')

        if m.get('AllocSizeMax') is not None:
            self.alloc_size_max = m.get('AllocSizeMax')

        if m.get('AllocSizePct50') is not None:
            self.alloc_size_pct_50 = m.get('AllocSizePct50')

        if m.get('AllocSizePct70') is not None:
            self.alloc_size_pct_70 = m.get('AllocSizePct70')

        if m.get('AllocSizePct90') is not None:
            self.alloc_size_pct_90 = m.get('AllocSizePct90')

        if m.get('CruxStack') is not None:
            self.crux_stack = m.get('CruxStack')

        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')

        if m.get('ErrorColumn') is not None:
            self.error_column = m.get('ErrorColumn')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ErrorCountGrowthRate') is not None:
            self.error_count_growth_rate = m.get('ErrorCountGrowthRate')

        if m.get('ErrorDeviceCount') is not None:
            self.error_device_count = m.get('ErrorDeviceCount')

        if m.get('ErrorDeviceCountGrowthRate') is not None:
            self.error_device_count_growth_rate = m.get('ErrorDeviceCountGrowthRate')

        if m.get('ErrorDeviceRate') is not None:
            self.error_device_rate = m.get('ErrorDeviceRate')

        if m.get('ErrorDeviceRateGrowthRate') is not None:
            self.error_device_rate_growth_rate = m.get('ErrorDeviceRateGrowthRate')

        if m.get('ErrorFileName') is not None:
            self.error_file_name = m.get('ErrorFileName')

        if m.get('ErrorLine') is not None:
            self.error_line = m.get('ErrorLine')

        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')

        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')

        if m.get('ErrorRateGrowthRate') is not None:
            self.error_rate_growth_rate = m.get('ErrorRateGrowthRate')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('FirstVersion') is not None:
            self.first_version = m.get('FirstVersion')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtLatest') is not None:
            self.gmt_latest = m.get('GmtLatest')

        if m.get('KeyLine') is not None:
            self.key_line = m.get('KeyLine')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Stack') is not None:
            self.stack = m.get('Stack')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('SymbolicStatus') is not None:
            self.symbolic_status = m.get('SymbolicStatus')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

