# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceVulStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vul_stat: main_models.DescribeInstanceVulStatisticsResponseBodyVulStat = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The statistics of the vulnerabilities.
        self.vul_stat = vul_stat

    def validate(self):
        if self.vul_stat:
            self.vul_stat.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vul_stat is not None:
            result['VulStat'] = self.vul_stat.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VulStat') is not None:
            temp_model = main_models.DescribeInstanceVulStatisticsResponseBodyVulStat()
            self.vul_stat = temp_model.from_map(m.get('VulStat'))

        return self

class DescribeInstanceVulStatisticsResponseBodyVulStat(DaraModel):
    def __init__(
        self,
        asap_count: str = None,
        later_count: str = None,
        nntf_count: str = None,
    ):
        # The number of high-risk vulnerabilities.
        self.asap_count = asap_count
        # The number of medium-risk vulnerabilities.
        self.later_count = later_count
        # The number of low-risk vulnerabilities.
        self.nntf_count = nntf_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count

        if self.later_count is not None:
            result['LaterCount'] = self.later_count

        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')

        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')

        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')

        return self

