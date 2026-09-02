# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataValue(DaraModel):
    def __init__(
        self,
        cve_num: int = None,
        emg_num: int = None,
        sys_num: int = None,
        cms_num: int = None,
        app_num: int = None,
        sca_num: int = None,
        vul_asap_sum: int = None,
        vul_later_sum: int = None,
        vul_nntf_sum: int = None,
        sys_asap_num: int = None,
    ):
        self.cve_num = cve_num
        self.emg_num = emg_num
        self.sys_num = sys_num
        self.cms_num = cms_num
        self.app_num = app_num
        self.sca_num = sca_num
        self.vul_asap_sum = vul_asap_sum
        self.vul_later_sum = vul_later_sum
        self.vul_nntf_sum = vul_nntf_sum
        self.sys_asap_num = sys_asap_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_num is not None:
            result['CveNum'] = self.cve_num

        if self.emg_num is not None:
            result['EmgNum'] = self.emg_num

        if self.sys_num is not None:
            result['SysNum'] = self.sys_num

        if self.cms_num is not None:
            result['CmsNum'] = self.cms_num

        if self.app_num is not None:
            result['AppNum'] = self.app_num

        if self.sca_num is not None:
            result['ScaNum'] = self.sca_num

        if self.vul_asap_sum is not None:
            result['VulAsapSum'] = self.vul_asap_sum

        if self.vul_later_sum is not None:
            result['VulLaterSum'] = self.vul_later_sum

        if self.vul_nntf_sum is not None:
            result['VulNntfSum'] = self.vul_nntf_sum

        if self.sys_asap_num is not None:
            result['SysAsapNum'] = self.sys_asap_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveNum') is not None:
            self.cve_num = m.get('CveNum')

        if m.get('EmgNum') is not None:
            self.emg_num = m.get('EmgNum')

        if m.get('SysNum') is not None:
            self.sys_num = m.get('SysNum')

        if m.get('CmsNum') is not None:
            self.cms_num = m.get('CmsNum')

        if m.get('AppNum') is not None:
            self.app_num = m.get('AppNum')

        if m.get('ScaNum') is not None:
            self.sca_num = m.get('ScaNum')

        if m.get('VulAsapSum') is not None:
            self.vul_asap_sum = m.get('VulAsapSum')

        if m.get('VulLaterSum') is not None:
            self.vul_later_sum = m.get('VulLaterSum')

        if m.get('VulNntfSum') is not None:
            self.vul_nntf_sum = m.get('VulNntfSum')

        if m.get('SysAsapNum') is not None:
            self.sys_asap_num = m.get('SysAsapNum')

        return self

