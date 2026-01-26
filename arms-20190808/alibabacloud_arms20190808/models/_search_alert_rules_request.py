# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchAlertRulesRequest(DaraModel):
    def __init__(
        self,
        alert_rule_id: str = None,
        app_type: str = None,
        current_page: int = None,
        page_size: int = None,
        pid: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        system_region_id: str = None,
        tags: List[main_models.SearchAlertRulesRequestTags] = None,
        title: str = None,
        type: str = None,
    ):
        # The id of AlertRule.
        self.alert_rule_id = alert_rule_id
        # The type of the application that is associated with the alert rule. Valid values:
        # 
        # *   `TRACE`: application
        # *   `RETCODE`: browser
        self.app_type = app_type
        # The page number of the page to return. Default value: `1`.
        self.current_page = current_page
        # The number of entries to return per page. Default value: `10`.
        self.page_size = page_size
        # The process identifier (PID) of the application that is associated with the alert rule. For more information about how to obtain the PID, see [Obtain the PID of an application](https://help.aliyun.com/document_detail/186100.html?spm=a2c4g.11186623.6.792.1b50654cqcDPyk#title-imy-7gj-qhr).
        self.pid = pid
        # The region ID of the alert data. For more information about the mappings between **RegionId** and **SystemRegionId**, see the detailed description below the table.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. You can obtain the resource group ID in the **Resource Management** console.
        self.resource_group_id = resource_group_id
        # The region ID of the alert rule. For more information about the mappings between **RegionId** and **SystemRegionId**, see the detailed description below the table.
        self.system_region_id = system_region_id
        # The list of tags.
        self.tags = tags
        # The alert rule name.
        self.title = title
        # The alert rule type. Valid values:
        # 
        # *   `1`: custom alert rules that are used to monitor drill-down data sets
        # *   `3`: custom alert rules that are used to monitor tiled data sets
        # *   `4`: alert rules that are used to monitor the browser, including the default frontend alert rules
        # *   `5`: alert rules that are used to monitor applications, including the default application alert rules
        # *   `6`: the default browser alert rules
        # *   `7`: the default application alert rules
        # *   `8`: Tracing Analysis alert rules
        # *   `101`: Prometheus alert rules
        self.type = type

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
        if self.alert_rule_id is not None:
            result['AlertRuleId'] = self.alert_rule_id

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_region_id is not None:
            result['SystemRegionId'] = self.system_region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRuleId') is not None:
            self.alert_rule_id = m.get('AlertRuleId')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemRegionId') is not None:
            self.system_region_id = m.get('SystemRegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.SearchAlertRulesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SearchAlertRulesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The following system preset fields are provided:
        # 
        # *   traceId: the ID of the trace.
        # *   serverApp: the name of the server application.
        # *   clientApp: the name of the client application.
        # *   service: the name of the operation.
        # *   rpc: the type of the call.
        # *   msOfSpan: the duration exceeds a specific value.
        # *   clientIp: the IP address of the client.
        # *   serverIp: the IP address of the server.
        # *   isError: specifies whether the call is abnormal.
        # *   hasTprof: contains only thread profiling.
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

