# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVulnerabilitiesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_num: int = None,
        vulnerabilities: List[main_models.ListVulnerabilitiesResponseBodyVulnerabilities] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of vulnerabilities that match the query conditions.
        self.total_num = total_num
        # The list of vulnerabilities.
        self.vulnerabilities = vulnerabilities

    def validate(self):
        if self.vulnerabilities:
            for v1 in self.vulnerabilities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        result['Vulnerabilities'] = []
        if self.vulnerabilities is not None:
            for k1 in self.vulnerabilities:
                result['Vulnerabilities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        self.vulnerabilities = []
        if m.get('Vulnerabilities') is not None:
            for k1 in m.get('Vulnerabilities'):
                temp_model = main_models.ListVulnerabilitiesResponseBodyVulnerabilities()
                self.vulnerabilities.append(temp_model.from_map(k1))

        return self

class ListVulnerabilitiesResponseBodyVulnerabilities(DaraModel):
    def __init__(
        self,
        cve_list: List[str] = None,
        description_en: str = None,
        description_zh: str = None,
        kbs: List[str] = None,
        product: str = None,
        release_time: int = None,
        title_en: str = None,
        title_zh: str = None,
        update_id: str = None,
        vul_device_count: int = None,
        vul_level: str = None,
        vul_type: str = None,
    ):
        # The list of CVE IDs corresponding to the vulnerability. An empty list is returned if no CVE is associated.
        self.cve_list = cve_list
        # The English description of the vulnerability.
        self.description_en = description_en
        # The Chinese description of the vulnerability.
        self.description_zh = description_zh
        # The list of Knowledge Base (KB) numbers corresponding to the vulnerability.
        self.kbs = kbs
        # The name of the product affected by the vulnerability.
        self.product = product
        # The release time of the vulnerability, in seconds as a UNIX timestamp.
        self.release_time = release_time
        # The English title of the vulnerability.
        self.title_en = title_en
        # The Chinese title of the vulnerability.
        self.title_zh = title_zh
        # The patch ID corresponding to the vulnerability. For Windows vulnerabilities, this is the Microsoft patch Update ID.
        self.update_id = update_id
        # The number of user endpoint devices affected by the vulnerability.
        self.vul_device_count = vul_device_count
        # The vulnerability risk level, mapped from the vendor risk level: Critical is mapped to High, Important is mapped to Mid, and others are mapped to Low. Valid values:
        # - **High**: high risk.
        # - **Mid**: medium risk.
        # - **Low**: low risk.
        self.vul_level = vul_level
        # The vulnerability type. Valid values:
        # - **windows**: Windows system vulnerability.
        # - **ai_agent**: AI Agent vulnerability.
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_list is not None:
            result['CveList'] = self.cve_list

        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en

        if self.description_zh is not None:
            result['DescriptionZh'] = self.description_zh

        if self.kbs is not None:
            result['Kbs'] = self.kbs

        if self.product is not None:
            result['Product'] = self.product

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.title_en is not None:
            result['TitleEn'] = self.title_en

        if self.title_zh is not None:
            result['TitleZh'] = self.title_zh

        if self.update_id is not None:
            result['UpdateId'] = self.update_id

        if self.vul_device_count is not None:
            result['VulDeviceCount'] = self.vul_device_count

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        if self.vul_type is not None:
            result['VulType'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveList') is not None:
            self.cve_list = m.get('CveList')

        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')

        if m.get('DescriptionZh') is not None:
            self.description_zh = m.get('DescriptionZh')

        if m.get('Kbs') is not None:
            self.kbs = m.get('Kbs')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('TitleEn') is not None:
            self.title_en = m.get('TitleEn')

        if m.get('TitleZh') is not None:
            self.title_zh = m.get('TitleZh')

        if m.get('UpdateId') is not None:
            self.update_id = m.get('UpdateId')

        if m.get('VulDeviceCount') is not None:
            self.vul_device_count = m.get('VulDeviceCount')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')

        return self

