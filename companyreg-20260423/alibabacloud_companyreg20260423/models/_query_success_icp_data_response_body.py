# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_companyreg20260423 import models as main_models
from darabonba.model import DaraModel

class QuerySuccessIcpDataResponseBody(DaraModel):
    def __init__(
        self,
        ba_success_data_with_risk_list: List[main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskList] = None,
        error_code: int = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.ba_success_data_with_risk_list = ba_success_data_with_risk_list
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.ba_success_data_with_risk_list:
            for v1 in self.ba_success_data_with_risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BaSuccessDataWithRiskList'] = []
        if self.ba_success_data_with_risk_list is not None:
            for k1 in self.ba_success_data_with_risk_list:
                result['BaSuccessDataWithRiskList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ba_success_data_with_risk_list = []
        if m.get('BaSuccessDataWithRiskList') is not None:
            for k1 in m.get('BaSuccessDataWithRiskList'):
                temp_model = main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskList()
                self.ba_success_data_with_risk_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskList(DaraModel):
    def __init__(
        self,
        app_list: List[main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListAppList] = None,
        icp_number: str = None,
        organizers_name: str = None,
        organizers_nature: str = None,
        responsible_person_name: str = None,
        risk_list: List[main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskList] = None,
        website_list: List[main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListWebsiteList] = None,
    ):
        self.app_list = app_list
        self.icp_number = icp_number
        self.organizers_name = organizers_name
        self.organizers_nature = organizers_nature
        self.responsible_person_name = responsible_person_name
        self.risk_list = risk_list
        self.website_list = website_list

    def validate(self):
        if self.app_list:
            for v1 in self.app_list:
                 if v1:
                    v1.validate()
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()
        if self.website_list:
            for v1 in self.website_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppList'] = []
        if self.app_list is not None:
            for k1 in self.app_list:
                result['AppList'].append(k1.to_map() if k1 else None)

        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number

        if self.organizers_name is not None:
            result['OrganizersName'] = self.organizers_name

        if self.organizers_nature is not None:
            result['OrganizersNature'] = self.organizers_nature

        if self.responsible_person_name is not None:
            result['ResponsiblePersonName'] = self.responsible_person_name

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        result['WebsiteList'] = []
        if self.website_list is not None:
            for k1 in self.website_list:
                result['WebsiteList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_list = []
        if m.get('AppList') is not None:
            for k1 in m.get('AppList'):
                temp_model = main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListAppList()
                self.app_list.append(temp_model.from_map(k1))

        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')

        if m.get('OrganizersName') is not None:
            self.organizers_name = m.get('OrganizersName')

        if m.get('OrganizersNature') is not None:
            self.organizers_nature = m.get('OrganizersNature')

        if m.get('ResponsiblePersonName') is not None:
            self.responsible_person_name = m.get('ResponsiblePersonName')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        self.website_list = []
        if m.get('WebsiteList') is not None:
            for k1 in m.get('WebsiteList'):
                temp_model = main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListWebsiteList()
                self.website_list.append(temp_model.from_map(k1))

        return self

class QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListWebsiteList(DaraModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        responsible_person_name: str = None,
        site_name: str = None,
        site_record_num: str = None,
    ):
        self.domain_list = domain_list
        self.responsible_person_name = responsible_person_name
        self.site_name = site_name
        self.site_record_num = site_record_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.responsible_person_name is not None:
            result['ResponsiblePersonName'] = self.responsible_person_name

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.site_record_num is not None:
            result['SiteRecordNum'] = self.site_record_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('ResponsiblePersonName') is not None:
            self.responsible_person_name = m.get('ResponsiblePersonName')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SiteRecordNum') is not None:
            self.site_record_num = m.get('SiteRecordNum')

        return self

class QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskList(DaraModel):
    def __init__(
        self,
        dead_line: str = None,
        risk_detail_list: List[main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskListRiskDetailList] = None,
    ):
        self.dead_line = dead_line
        self.risk_detail_list = risk_detail_list

    def validate(self):
        if self.risk_detail_list:
            for v1 in self.risk_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dead_line is not None:
            result['DeadLine'] = self.dead_line

        result['RiskDetailList'] = []
        if self.risk_detail_list is not None:
            for k1 in self.risk_detail_list:
                result['RiskDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLine') is not None:
            self.dead_line = m.get('DeadLine')

        self.risk_detail_list = []
        if m.get('RiskDetailList') is not None:
            for k1 in m.get('RiskDetailList'):
                temp_model = main_models.QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskListRiskDetailList()
                self.risk_detail_list.append(temp_model.from_map(k1))

        return self

class QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListRiskListRiskDetailList(DaraModel):
    def __init__(
        self,
        rectify_suggest_list: List[str] = None,
        risk_source: str = None,
    ):
        self.rectify_suggest_list = rectify_suggest_list
        self.risk_source = risk_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rectify_suggest_list is not None:
            result['RectifySuggestList'] = self.rectify_suggest_list

        if self.risk_source is not None:
            result['RiskSource'] = self.risk_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RectifySuggestList') is not None:
            self.rectify_suggest_list = m.get('RectifySuggestList')

        if m.get('RiskSource') is not None:
            self.risk_source = m.get('RiskSource')

        return self



class QuerySuccessIcpDataResponseBodyBaSuccessDataWithRiskListAppList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_record_num: str = None,
        domain_list: List[str] = None,
        responsible_person_name: str = None,
    ):
        self.app_name = app_name
        self.app_record_num = app_record_num
        self.domain_list = domain_list
        self.responsible_person_name = responsible_person_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_record_num is not None:
            result['AppRecordNum'] = self.app_record_num

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.responsible_person_name is not None:
            result['ResponsiblePersonName'] = self.responsible_person_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppRecordNum') is not None:
            self.app_record_num = m.get('AppRecordNum')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('ResponsiblePersonName') is not None:
            self.responsible_person_name = m.get('ResponsiblePersonName')

        return self

