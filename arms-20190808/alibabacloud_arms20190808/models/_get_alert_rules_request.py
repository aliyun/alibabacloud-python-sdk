# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetAlertRulesRequest(DaraModel):
    def __init__(
        self,
        alert_ids: str = None,
        alert_names: str = None,
        alert_status: str = None,
        alert_type: str = None,
        biz_region_id: str = None,
        cluster_id: str = None,
        page: int = None,
        product_code: str = None,
        region_id: str = None,
        size: int = None,
        tags: List[main_models.GetAlertRulesRequestTags] = None,
    ):
        # The unique IDs of alert rules.
        # 
        # *   If you do not specify this parameter, the API operation does not filter alert rules based on their IDs.
        # *   If you specify this parameter, the API operation returns only the information of the specified alert rules. Other filter conditions also take effect.
        # 
        # > When you call the GetAlertRules operation, you can specify other request parameters to obtain the AlertIds parameter from the response. Then, you can specify the AlertIds parameter to query the specified alert rules.
        self.alert_ids = alert_ids
        # The names of alert rules. When you create alert rules of the new version, you cannot specify duplicate names. However, existing alert rules may have duplicate names. Therefore, the **AlertName** parameter does not uniquely identify an alert rule.
        # 
        # *   If you do not specify this parameter, the API operation does not filter alert rules based on their names.
        # *   If you specify this parameter, the API operation returns only the information of the specified alert rules. Other filter conditions also take effect.
        self.alert_names = alert_names
        # The status of the alert rule. Valid values:
        # 
        # *   RUNNING
        # *   STOPPED
        # *   PAUSED
        # 
        # >  The PAUSED state indicates an abnormal and paused alert rule. This may result from excessively large threshold values or deleted associated clusters.
        self.alert_status = alert_status
        # The type of the alert rule. This parameter is required for the new version of Alert Management. Valid values:
        # 
        # *   APPLICATION_MONITORING_ALERT_RULE: alert rule for Application Monitoring
        # *   BROWSER_MONITORING_ALERT_RULE: alert rule for Browser Monitoring
        # *   PROMETHEUS_MONITORING_ALERT_RULE: alert rule for Managed Service for Prometheus
        self.alert_type = alert_type
        self.biz_region_id = biz_region_id
        # The ID of the monitored cluster.
        self.cluster_id = cluster_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # You do not need to configure this parameter.
        self.product_code = product_code
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of alert rules to return on each page.
        # 
        # This parameter is required.
        self.size = size
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids

        if self.alert_names is not None:
            result['AlertNames'] = self.alert_names

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page is not None:
            result['Page'] = self.page

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size is not None:
            result['Size'] = self.size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')

        if m.get('AlertNames') is not None:
            self.alert_names = m.get('AlertNames')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAlertRulesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetAlertRulesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

