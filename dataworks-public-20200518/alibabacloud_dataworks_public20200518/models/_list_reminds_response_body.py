# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListRemindsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListRemindsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListRemindsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRemindsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        reminds: List[main_models.ListRemindsResponseBodyDataReminds] = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The list of custom alert rules.
        self.reminds = reminds
        # The total number of custom alert rules returned.
        self.total_count = total_count

    def validate(self):
        if self.reminds:
            for v1 in self.reminds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Reminds'] = []
        if self.reminds is not None:
            for k1 in self.reminds:
                result['Reminds'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.reminds = []
        if m.get('Reminds') is not None:
            for k1 in m.get('Reminds'):
                temp_model = main_models.ListRemindsResponseBodyDataReminds()
                self.reminds.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRemindsResponseBodyDataReminds(DaraModel):
    def __init__(
        self,
        alert_methods: List[str] = None,
        alert_targets: List[str] = None,
        alert_unit: str = None,
        baseline_ids: List[int] = None,
        biz_process_ids: List[int] = None,
        dnd_end: str = None,
        dnd_start: str = None,
        founder: str = None,
        node_ids: List[int] = None,
        project_ids: List[int] = None,
        remind_id: int = None,
        remind_name: str = None,
        remind_type: str = None,
        remind_unit: str = None,
        useflag: bool = None,
    ):
        # The notification method. Valid values: MAIL, SMS, and PHONE. The value MAIL indicates that the notification is sent by email. Only DataWorks Professional Edition and more advanced editions support the PHONE notification method.
        self.alert_methods = alert_methods
        # The IDs of the Alibaba Cloud accounts used by alert recipients.
        self.alert_targets = alert_targets
        # The alert recipient. Valid values: OWNER and OTHER. The value OWNER indicates the node owner. The value OTHER indicates a specified user.
        self.alert_unit = alert_unit
        # The IDs of the baselines to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is BASELINE.
        self.baseline_ids = baseline_ids
        # The IDs of the workflows to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is BIZPROCESS.
        self.biz_process_ids = biz_process_ids
        # The end time of the quiet hours. The time is in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_end = dnd_end
        # The start time of the quiet hours. The time is in the hh:mm format. Valid values of hh: [0,23]. Valid values of mm: [0,59].
        self.dnd_start = dnd_start
        # The ID of the Alibaba Cloud account used by the rule creator.
        self.founder = founder
        # The IDs of the nodes to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is NODE.
        self.node_ids = node_ids
        # The IDs of the workspaces to which the custom alert rule is applied. This parameter is returned if the value of the RemindUnit parameter is PROJECT.
        self.project_ids = project_ids
        # The custom alert rule ID.
        self.remind_id = remind_id
        # The name of the custom alert rule.
        self.remind_name = remind_name
        # The condition that triggers an alert. Valid values: FINISHED, UNFINISHED, ERROR, CYCLE_UNFINISHED, and TIMEOUT.
        self.remind_type = remind_type
        # The type of the object to which the custom alert rule is applied. Valid values: NODE, BASELINE, PROJECT, and BIZPROCESS. The value NODE indicates a node. The value BASELINE indicates a baseline. The value PROJECT indicates a workspace. The value BIZPROCESS indicates a workflow.
        self.remind_unit = remind_unit
        # Indicates whether the custom alert rule is enabled. Valid values: true and false.
        self.useflag = useflag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_methods is not None:
            result['AlertMethods'] = self.alert_methods

        if self.alert_targets is not None:
            result['AlertTargets'] = self.alert_targets

        if self.alert_unit is not None:
            result['AlertUnit'] = self.alert_unit

        if self.baseline_ids is not None:
            result['BaselineIds'] = self.baseline_ids

        if self.biz_process_ids is not None:
            result['BizProcessIds'] = self.biz_process_ids

        if self.dnd_end is not None:
            result['DndEnd'] = self.dnd_end

        if self.dnd_start is not None:
            result['DndStart'] = self.dnd_start

        if self.founder is not None:
            result['Founder'] = self.founder

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        if self.remind_name is not None:
            result['RemindName'] = self.remind_name

        if self.remind_type is not None:
            result['RemindType'] = self.remind_type

        if self.remind_unit is not None:
            result['RemindUnit'] = self.remind_unit

        if self.useflag is not None:
            result['Useflag'] = self.useflag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertMethods') is not None:
            self.alert_methods = m.get('AlertMethods')

        if m.get('AlertTargets') is not None:
            self.alert_targets = m.get('AlertTargets')

        if m.get('AlertUnit') is not None:
            self.alert_unit = m.get('AlertUnit')

        if m.get('BaselineIds') is not None:
            self.baseline_ids = m.get('BaselineIds')

        if m.get('BizProcessIds') is not None:
            self.biz_process_ids = m.get('BizProcessIds')

        if m.get('DndEnd') is not None:
            self.dnd_end = m.get('DndEnd')

        if m.get('DndStart') is not None:
            self.dnd_start = m.get('DndStart')

        if m.get('Founder') is not None:
            self.founder = m.get('Founder')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        if m.get('RemindName') is not None:
            self.remind_name = m.get('RemindName')

        if m.get('RemindType') is not None:
            self.remind_type = m.get('RemindType')

        if m.get('RemindUnit') is not None:
            self.remind_unit = m.get('RemindUnit')

        if m.get('Useflag') is not None:
            self.useflag = m.get('Useflag')

        return self

