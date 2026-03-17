# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DiscribeSmartAccessGatewayDiagnosisReportResponseBody(DaraModel):
    def __init__(
        self,
        diagnose_result: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResult = None,
        request_id: str = None,
    ):
        # The diagnosis report of the SAG device.
        self.diagnose_result = diagnose_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.diagnose_result:
            self.diagnose_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_result is not None:
            result['DiagnoseResult'] = self.diagnose_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseResult') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResult()
            self.diagnose_result = temp_model.from_map(m.get('DiagnoseResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResult(DaraModel):
    def __init__(
        self,
        box_type: str = None,
        box_version: str = None,
        details: List[main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetails] = None,
        diagnose_id: str = None,
        end_time: int = None,
        finished_number: int = None,
        instance_id: str = None,
        level: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultLevel = None,
        monitor_version: str = None,
        percent: int = None,
        report_slssuccess: int = None,
        sn: str = None,
        start_time: int = None,
        state: str = None,
        statistics: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultStatistics = None,
        store_type: str = None,
        total_number: int = None,
        uid: str = None,
        user_level: str = None,
    ):
        # The model of the SAG device.
        # 
        # *   **sag-1000**
        # *   **sag-100WM**
        self.box_type = box_type
        # The version of the SAG device.
        self.box_version = box_version
        # The list of diagnoses that are returned.
        self.details = details
        # The ID of the diagnosis.
        self.diagnose_id = diagnose_id
        # The timestamp when the system finishes diagnosing the item.
        self.end_time = end_time
        # The number of items that are diagnosed.
        self.finished_number = finished_number
        # The ID of the SAG instance.
        self.instance_id = instance_id
        # The diagnosis level.
        self.level = level
        # The version of the monitoring feature that is used by the SAG device.
        self.monitor_version = monitor_version
        # The completion percentage of the diagnosis report.
        self.percent = percent
        # The status of the diagnosis report to be uploaded to Log Service.
        # 
        # *   **0**: The system failed to upload the report.
        # *   **1**: The system has uploaded the report to Log Service.
        self.report_slssuccess = report_slssuccess
        # The serial number of the SAG device.
        self.sn = sn
        # The timestamp when the system starts to diagnose the item.
        self.start_time = start_time
        # The diagnosis status. Valid values:
        # 
        # *   **processing**: The SAG device is being diagnosed.
        # *   **finished**: The SAG device is diagnosed.
        # *   **failed**: The system failed to diagnose the SAG device.
        # *   **error**: A diagnostic error occurred.
        # *   **upload_to_sls_fail**: The system failed to upload the diagnosis report.
        self.state = state
        # The overall diagnosis level.
        self.statistics = statistics
        # The storage type.
        # 
        # The value is set to **both**, which indicates that the data is stored in the SAG device and Log Service.
        self.store_type = store_type
        # The total number of entries returned.
        self.total_number = total_number
        # The user ID (UID) of the Alibaba Cloud account to which the SAG instance belongs.
        self.uid = uid
        # The type of user that initiated the diagnostics. The value is set to **user**.
        self.user_level = user_level

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.level:
            self.level.validate()
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.box_type is not None:
            result['BoxType'] = self.box_type

        if self.box_version is not None:
            result['BoxVersion'] = self.box_version

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finished_number is not None:
            result['FinishedNumber'] = self.finished_number

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.level is not None:
            result['Level'] = self.level.to_map()

        if self.monitor_version is not None:
            result['MonitorVersion'] = self.monitor_version

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.report_slssuccess is not None:
            result['ReportSLSSuccess'] = self.report_slssuccess

        if self.sn is not None:
            result['SN'] = self.sn

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        if self.store_type is not None:
            result['StoreType'] = self.store_type

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        if self.uid is not None:
            result['UId'] = self.uid

        if self.user_level is not None:
            result['UserLevel'] = self.user_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoxType') is not None:
            self.box_type = m.get('BoxType')

        if m.get('BoxVersion') is not None:
            self.box_version = m.get('BoxVersion')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishedNumber') is not None:
            self.finished_number = m.get('FinishedNumber')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Level') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultLevel()
            self.level = temp_model.from_map(m.get('Level'))

        if m.get('MonitorVersion') is not None:
            self.monitor_version = m.get('MonitorVersion')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('ReportSLSSuccess') is not None:
            self.report_slssuccess = m.get('ReportSLSSuccess')

        if m.get('SN') is not None:
            self.sn = m.get('SN')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Statistics') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        if m.get('UId') is not None:
            self.uid = m.get('UId')

        if m.get('UserLevel') is not None:
            self.user_level = m.get('UserLevel')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultStatistics(DaraModel):
    def __init__(
        self,
        error: int = None,
        info: int = None,
        total: int = None,
        warning: int = None,
    ):
        # The number of items of the **ERROR** level.
        self.error = error
        # The number of items of the **INFO** level.
        self.info = info
        # The total number of items.
        self.total = total
        # The number of items of the **WARNING** level.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.info is not None:
            result['Info'] = self.info

        if self.total is not None:
            result['Total'] = self.total

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultLevel(DaraModel):
    def __init__(
        self,
        biz: str = None,
        configuration: str = None,
        total: str = None,
    ):
        # The diagnosis level of the service quality.
        self.biz = biz
        # The diagnosis level of the SAG configuration.
        self.configuration = configuration
        # The overall diagnosis level.
        # 
        # *   **error**: severe
        # *   **warning**: warning
        # *   **info**: normal
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.configuration is not None:
            result['Configuration'] = self.configuration

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetails(DaraModel):
    def __init__(
        self,
        items: List[main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItems] = None,
        statistics: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsStatistics = None,
        type: str = None,
    ):
        # The list of items diagnosed.
        self.items = items
        # The information about items of each diagnosis level for the current diagnosis type.
        self.statistics = statistics
        # The type of the diagnosis. Valid values:
        # 
        # *   **config**: SAG configuration
        # *   **internet**: quality of connections to the Internet
        # *   **biz**: service quality
        self.type = type

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Statistics') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsStatistics(DaraModel):
    def __init__(
        self,
        error: int = None,
        info: int = None,
        total: int = None,
        warning: int = None,
    ):
        # The number of items of the **ERROR** level.
        self.error = error
        # The number of items of the **INFO** level.
        self.info = info
        # The total number of items for the current diagnosis type.
        self.total = total
        # The number of items of the **WARNING** level.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.info is not None:
            result['Info'] = self.info

        if self.total is not None:
            result['Total'] = self.total

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItems(DaraModel):
    def __init__(
        self,
        cn: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsCN = None,
        en: main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsEN = None,
        end_time: int = None,
        item_name: str = None,
        level: str = None,
        start_time: int = None,
        type: str = None,
    ):
        # The diagnosis report in Chinese.
        self.cn = cn
        # The diagnosis report in English.
        self.en = en
        # The timestamp when the system finishes diagnosing the item.
        self.end_time = end_time
        # The name of the item, which is the unique identifier of the item.
        self.item_name = item_name
        # The diagnosis level of the item. Valid values:
        # 
        # *   **error**: severe
        # *   **warning**: warning
        # *   **info**: normal
        self.level = level
        # The timestamp when the system starts to diagnose the item.
        self.start_time = start_time
        # The type of the item. Valid values:
        # 
        # *   **config**: SAG configuration
        # *   **internet**: quality of connections to the Internet
        # *   **biz**: service quality
        self.type = type

    def validate(self):
        if self.cn:
            self.cn.validate()
        if self.en:
            self.en.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn is not None:
            result['CN'] = self.cn.to_map()

        if self.en is not None:
            result['EN'] = self.en.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.level is not None:
            result['Level'] = self.level

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CN') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsCN()
            self.cn = temp_model.from_map(m.get('CN'))

        if m.get('EN') is not None:
            temp_model = main_models.DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsEN()
            self.en = temp_model.from_map(m.get('EN'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsEN(DaraModel):
    def __init__(
        self,
        advice: List[str] = None,
        details: List[str] = None,
        item_level: str = None,
        item_name: str = None,
        item_type: str = None,
    ):
        # The suggestion for the diagnosis.
        self.advice = advice
        # The diagnosis.
        self.details = details
        # The diagnosis level of the item. Valid values:
        # 
        # *   **ERROR**: indicates that the item has an issue that may affect your services. We recommend that you handle the issue at the earliest opportunity.
        # *   **WARNING**: indicates that the item has an issue. You can handle the issue based on your business requirements.
        # *   **INFO**: indicates that the item is working as expected. No additional operation is required.
        self.item_level = item_level
        # The name of the item.
        self.item_name = item_name
        # The type of the item. Valid values:
        # 
        # *   **Config**: **SAG configuration**
        # *   **Service**: **service quality**
        # *   **Internet**: **quality of connections to the Internet**
        self.item_type = item_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.details is not None:
            result['Details'] = self.details

        if self.item_level is not None:
            result['ItemLevel'] = self.item_level

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ItemLevel') is not None:
            self.item_level = m.get('ItemLevel')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        return self

class DiscribeSmartAccessGatewayDiagnosisReportResponseBodyDiagnoseResultDetailsItemsCN(DaraModel):
    def __init__(
        self,
        advice: List[str] = None,
        details: List[str] = None,
        item_level: str = None,
        item_name: str = None,
        item_type: str = None,
    ):
        # The suggestion for the diagnosis.
        self.advice = advice
        # The diagnosis.
        self.details = details
        # The diagnosis level of the item. Valid values:
        # 
        # *   **ERROR**: indicates that the item has an issue that may affect your services. We recommend that you handle the issue at the earliest opportunity.
        # *   **WARNING**: indicates that the item has an issue. You can handle the issue based on your business requirements.
        # *   **INFO**: indicates that the item is working as expected. No additional operation is required.
        self.item_level = item_level
        # The name of the item.
        self.item_name = item_name
        # The type of the item. Valid values:
        # 
        # *   **Config**: **SAG configuration**
        # *   **Service**: **service quality**
        # *   **Internet**: **quality of connections to the Internet**
        self.item_type = item_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.details is not None:
            result['Details'] = self.details

        if self.item_level is not None:
            result['ItemLevel'] = self.item_level

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('ItemLevel') is not None:
            self.item_level = m.get('ItemLevel')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        return self

