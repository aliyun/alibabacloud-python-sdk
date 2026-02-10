# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVulNumStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        app_cnt: int = None,
        app_num: int = None,
        cms_dealed_total_num: int = None,
        cms_num: int = None,
        cve_num: int = None,
        emg_num: int = None,
        request_id: str = None,
        sca_num: int = None,
        sys_num: int = None,
        vul_asap_sum: int = None,
        vul_dealed_total_num: int = None,
        vul_later_sum: int = None,
        vul_nntf_sum: int = None,
    ):
        # The number of application vulnerabilities that are detected on the asset by using the web scanner.
        self.app_cnt = app_cnt
        # The number of application vulnerabilities that are detected on the asset by using the web scanner.
        self.app_num = app_num
        # The number of Web-CMS vulnerabilities that are handled.
        self.cms_dealed_total_num = cms_dealed_total_num
        # The number of Web-CMS vulnerabilities that are detected on the asset.
        self.cms_num = cms_num
        # The number of Linux software vulnerabilities that are detected on the asset.
        self.cve_num = cve_num
        # The number of urgent vulnerabilities that are detected on the asset.
        self.emg_num = emg_num
        # The request ID.
        self.request_id = request_id
        # The number of middleware vulnerabilities that are detected on the asset.
        self.sca_num = sca_num
        # The number of Windows system vulnerabilities that are detected on the asset.
        self.sys_num = sys_num
        # The number of vulnerabilities that have the high priority.
        self.vul_asap_sum = vul_asap_sum
        # The number of vulnerabilities that are handled.
        self.vul_dealed_total_num = vul_dealed_total_num
        # The number of vulnerabilities that have the medium priority.
        self.vul_later_sum = vul_later_sum
        # The number of vulnerabilities that have the low priority.
        self.vul_nntf_sum = vul_nntf_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_cnt is not None:
            result['AppCnt'] = self.app_cnt

        if self.app_num is not None:
            result['AppNum'] = self.app_num

        if self.cms_dealed_total_num is not None:
            result['CmsDealedTotalNum'] = self.cms_dealed_total_num

        if self.cms_num is not None:
            result['CmsNum'] = self.cms_num

        if self.cve_num is not None:
            result['CveNum'] = self.cve_num

        if self.emg_num is not None:
            result['EmgNum'] = self.emg_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sca_num is not None:
            result['ScaNum'] = self.sca_num

        if self.sys_num is not None:
            result['SysNum'] = self.sys_num

        if self.vul_asap_sum is not None:
            result['VulAsapSum'] = self.vul_asap_sum

        if self.vul_dealed_total_num is not None:
            result['VulDealedTotalNum'] = self.vul_dealed_total_num

        if self.vul_later_sum is not None:
            result['VulLaterSum'] = self.vul_later_sum

        if self.vul_nntf_sum is not None:
            result['VulNntfSum'] = self.vul_nntf_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCnt') is not None:
            self.app_cnt = m.get('AppCnt')

        if m.get('AppNum') is not None:
            self.app_num = m.get('AppNum')

        if m.get('CmsDealedTotalNum') is not None:
            self.cms_dealed_total_num = m.get('CmsDealedTotalNum')

        if m.get('CmsNum') is not None:
            self.cms_num = m.get('CmsNum')

        if m.get('CveNum') is not None:
            self.cve_num = m.get('CveNum')

        if m.get('EmgNum') is not None:
            self.emg_num = m.get('EmgNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScaNum') is not None:
            self.sca_num = m.get('ScaNum')

        if m.get('SysNum') is not None:
            self.sys_num = m.get('SysNum')

        if m.get('VulAsapSum') is not None:
            self.vul_asap_sum = m.get('VulAsapSum')

        if m.get('VulDealedTotalNum') is not None:
            self.vul_dealed_total_num = m.get('VulDealedTotalNum')

        if m.get('VulLaterSum') is not None:
            self.vul_later_sum = m.get('VulLaterSum')

        if m.get('VulNntfSum') is not None:
            self.vul_nntf_sum = m.get('VulNntfSum')

        return self

