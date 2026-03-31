# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeAlertsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeAlertsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeAlertsResponseBodyDataPageInfo = None,
        response_data: List[main_models.DescribeAlertsResponseBodyDataResponseData] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The detailed data.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeAlertsResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.DescribeAlertsResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class DescribeAlertsResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_desc: str = None,
        alert_desc_code: str = None,
        alert_desc_en: str = None,
        alert_detail: str = None,
        alert_info_list: List[main_models.DescribeAlertsResponseBodyDataResponseDataAlertInfoList] = None,
        alert_level: str = None,
        alert_name: str = None,
        alert_name_code: str = None,
        alert_name_en: str = None,
        alert_src_prod: str = None,
        alert_src_prod_module: str = None,
        alert_status: str = None,
        alert_title: str = None,
        alert_title_en: str = None,
        alert_type: str = None,
        alert_type_code: str = None,
        alert_type_en: str = None,
        alert_uuid: str = None,
        asset_list: str = None,
        att_ck: str = None,
        cloud_code: str = None,
        detection_rule_id: str = None,
        end_time: str = None,
        entity_list: str = None,
        extend_content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_uuid: str = None,
        investigation_report: str = None,
        is_defend: str = None,
        log_time: str = None,
        log_uuid: str = None,
        main_user_id: int = None,
        occur_time: str = None,
        product_id: str = None,
        start_time: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
        vendor_id: str = None,
    ):
        # The description of the alert.
        self.alert_desc = alert_desc
        # The internal code of the alert description.
        self.alert_desc_code = alert_desc_code
        # The description of the alert in English.
        self.alert_desc_en = alert_desc_en
        # The details of the alert.
        self.alert_detail = alert_detail
        # The displayed details of the alert.
        self.alert_info_list = alert_info_list
        # The threat level. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.alert_level = alert_level
        # The name of the alert.
        self.alert_name = alert_name
        # The internal code of the alert name.
        self.alert_name_code = alert_name_code
        # The name of the alert in English.
        self.alert_name_en = alert_name_en
        # The service for which the alert associated with the event is generated.
        self.alert_src_prod = alert_src_prod
        # The sub-module of ther alert source.
        self.alert_src_prod_module = alert_src_prod_module
        self.alert_status = alert_status
        # The title of the alert.
        self.alert_title = alert_title
        # The title of the alert in English.
        self.alert_title_en = alert_title_en
        # The alert type.
        self.alert_type = alert_type
        # The internal code of the alert type.
        self.alert_type_code = alert_type_code
        # The type of the alert in English.
        self.alert_type_en = alert_type_en
        # The UUID of the alert.
        self.alert_uuid = alert_uuid
        # The details of the asset.
        self.asset_list = asset_list
        # The tag of the ATT\\&CK attack.
        self.att_ck = att_ck
        # The cloud code. Valid values:
        # 
        # *   aliyun: Alibaba Cloud
        # *   qcloud: Tencent Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        self.detection_rule_id = detection_rule_id
        # The time when the alert was closed.
        self.end_time = end_time
        self.entity_list = entity_list
        self.extend_content = extend_content
        # The time when the alert was received.
        self.gmt_create = gmt_create
        # The time when the alert was last updated.
        self.gmt_modified = gmt_modified
        # The unique ID of the alert.
        self.id = id
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        self.investigation_report = investigation_report
        # Indicates whether an attack is defended. Valid values:
        # 
        # *   0: detected.
        # *   1: blocked.
        self.is_defend = is_defend
        # The time when the alert was recorded.
        self.log_time = log_time
        # The UUID of the alert log.
        self.log_uuid = log_uuid
        # The ID of the Alibaba Cloud account that is associated with the alert in SIEM.
        self.main_user_id = main_user_id
        # The time when the alert is triggered.
        self.occur_time = occur_time
        self.product_id = product_id
        # The time at which the alert was first generated.
        self.start_time = start_time
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id
        self.sub_user_name = sub_user_name
        self.vendor_id = vendor_id

    def validate(self):
        if self.alert_info_list:
            for v1 in self.alert_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_desc is not None:
            result['AlertDesc'] = self.alert_desc

        if self.alert_desc_code is not None:
            result['AlertDescCode'] = self.alert_desc_code

        if self.alert_desc_en is not None:
            result['AlertDescEn'] = self.alert_desc_en

        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail

        result['AlertInfoList'] = []
        if self.alert_info_list is not None:
            for k1 in self.alert_info_list:
                result['AlertInfoList'].append(k1.to_map() if k1 else None)

        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_name_code is not None:
            result['AlertNameCode'] = self.alert_name_code

        if self.alert_name_en is not None:
            result['AlertNameEn'] = self.alert_name_en

        if self.alert_src_prod is not None:
            result['AlertSrcProd'] = self.alert_src_prod

        if self.alert_src_prod_module is not None:
            result['AlertSrcProdModule'] = self.alert_src_prod_module

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title

        if self.alert_title_en is not None:
            result['AlertTitleEn'] = self.alert_title_en

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_type_code is not None:
            result['AlertTypeCode'] = self.alert_type_code

        if self.alert_type_en is not None:
            result['AlertTypeEn'] = self.alert_type_en

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.asset_list is not None:
            result['AssetList'] = self.asset_list

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.entity_list is not None:
            result['EntityList'] = self.entity_list

        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.investigation_report is not None:
            result['InvestigationReport'] = self.investigation_report

        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.log_uuid is not None:
            result['LogUuid'] = self.log_uuid

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.occur_time is not None:
            result['OccurTime'] = self.occur_time

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDesc') is not None:
            self.alert_desc = m.get('AlertDesc')

        if m.get('AlertDescCode') is not None:
            self.alert_desc_code = m.get('AlertDescCode')

        if m.get('AlertDescEn') is not None:
            self.alert_desc_en = m.get('AlertDescEn')

        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')

        self.alert_info_list = []
        if m.get('AlertInfoList') is not None:
            for k1 in m.get('AlertInfoList'):
                temp_model = main_models.DescribeAlertsResponseBodyDataResponseDataAlertInfoList()
                self.alert_info_list.append(temp_model.from_map(k1))

        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertNameCode') is not None:
            self.alert_name_code = m.get('AlertNameCode')

        if m.get('AlertNameEn') is not None:
            self.alert_name_en = m.get('AlertNameEn')

        if m.get('AlertSrcProd') is not None:
            self.alert_src_prod = m.get('AlertSrcProd')

        if m.get('AlertSrcProdModule') is not None:
            self.alert_src_prod_module = m.get('AlertSrcProdModule')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')

        if m.get('AlertTitleEn') is not None:
            self.alert_title_en = m.get('AlertTitleEn')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertTypeCode') is not None:
            self.alert_type_code = m.get('AlertTypeCode')

        if m.get('AlertTypeEn') is not None:
            self.alert_type_en = m.get('AlertTypeEn')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('AssetList') is not None:
            self.asset_list = m.get('AssetList')

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EntityList') is not None:
            self.entity_list = m.get('EntityList')

        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('InvestigationReport') is not None:
            self.investigation_report = m.get('InvestigationReport')

        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('LogUuid') is not None:
            self.log_uuid = m.get('LogUuid')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('OccurTime') is not None:
            self.occur_time = m.get('OccurTime')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

class DescribeAlertsResponseBodyDataResponseDataAlertInfoList(DaraModel):
    def __init__(
        self,
        key: str = None,
        key_name: str = None,
        values: str = None,
    ):
        # The attribute key.
        self.key = key
        # The name of the key.
        self.key_name = key_name
        # The value of the key.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class DescribeAlertsResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

