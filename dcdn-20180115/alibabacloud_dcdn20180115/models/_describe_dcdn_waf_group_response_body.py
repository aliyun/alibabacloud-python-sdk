# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafGroupResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[main_models.DescribeDcdnWafGroupResponseBodyRules] = None,
        subscribe: str = None,
        template_id: int = None,
        total_count: int = None,
    ):
        # The ID of the custom WAF rule group.
        self.id = id
        # The name of the WAF rule group.
        self.name = name
        # The page number of the page returned.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The configurations of the rule.
        self.rules = rules
        # Indicates whether to enable subscription. Valid values:
        # 
        # *   **on:**
        # *   **off**
        self.subscribe = subscribe
        # The ID of the template.
        self.template_id = template_id
        # The total number of rules that are filtered out.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.subscribe is not None:
            result['Subscribe'] = self.subscribe

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeDcdnWafGroupResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Subscribe') is not None:
            self.subscribe = m.get('Subscribe')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnWafGroupResponseBodyRules(DaraModel):
    def __init__(
        self,
        application_type: int = None,
        cve_id: str = None,
        cve_url: str = None,
        description: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        protection_type: int = None,
        risk_level: int = None,
    ):
        # The type of the application. Valid values:
        # 
        # *   **0**: Common
        # *   **1**: WordPress
        # *   **2**: DedeCMS
        # *   **3**: Discuz
        # *   **4**: PHP CMS
        # *   **5**: ECShop
        # *   **6**: ShopEX
        # *   **7**: Drupal
        # *   **8**: Joomla
        # *   **9**: MetInfo
        # *   **10**: Struts2
        # *   **11**: Spring Boot
        # *   **12**: JBoss
        # *   **13**: WebLogic
        # *   **14**: WebSphere
        # *   **15**: Tomcat
        # *   **16**: Elastic Search
        # *   **18**: ThinkPHP
        # *   **19**: Fastjson
        # *   **20**: ImageMagick
        # *   **21**: PHPWind
        # *   **22**: phpMyAdmin
        # *   **23**: Resin
        # *   **24**: IIS
        # *   **99**: Others
        self.application_type = application_type
        # The Common Vulnerabilities and Exposures (CVE) ID of the related vulnerability.
        self.cve_id = cve_id
        # The CVE link.
        self.cve_url = cve_url
        # The description of the WAF rule.
        self.description = description
        # The time when the rule was modified.
        self.gmt_modified = gmt_modified
        # The ID of the custom WAF rule.
        self.id = id
        # The name of the WAF rule.
        self.name = name
        # Protection type Valid values:
        # 
        # *   **11**: SQL injection
        # *   **12**: cross-site scripting (XSS)
        # *   **13**: code execution
        # *   **14**: carriage return line feeds (CRLF)
        # *   **15**: local file inclusion
        # *   **16**: remote file inclusion
        # *   **17**: webshells
        # *   **19**: cross-site request forgery
        # *   **20**: others
        # *   **21**: SEMA
        self.protection_type = protection_type
        # The risk level of the resources that do not comply with the managed rule. Valid values:
        # 
        # *   **1**: high risk
        # *   **2**: medium risk
        # *   **3**: low risk
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.cve_url is not None:
            result['CveUrl'] = self.cve_url

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.protection_type is not None:
            result['ProtectionType'] = self.protection_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('CveUrl') is not None:
            self.cve_url = m.get('CveUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtectionType') is not None:
            self.protection_type = m.get('ProtectionType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

