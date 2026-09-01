# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProcessTasksRequest(DaraModel):
    def __init__(
        self,
        alert_id: str = None,
        direction: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        event_uuid: str = None,
        execute_uuid: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        param_content: str = None,
        process_action_end: int = None,
        process_action_start: int = None,
        process_remove_end: int = None,
        process_remove_start: int = None,
        process_strategy_uuid: str = None,
        req_uuid: str = None,
        response_rule_id: str = None,
        scene_code: str = None,
        scope: str = None,
        source: str = None,
        task_id: str = None,
        task_status: str = None,
        trigger_source: str = None,
        yun_code: str = None,
    ):
        self.alert_id = alert_id
        # The sort direction. Valid values:
        # 
        # - **desc**: Descending (default).
        # - **asc**: Ascending.
        self.direction = direction
        # The name of the entity to be disposed.
        self.entity_name = entity_name
        # The type of the entity to be disposed. Valid values:
        # 
        # - **ip**: IP address entity.
        # - **file**: File entity.
        # - **process**: Process entity.
        self.entity_type = entity_type
        # The UUID of the entity.
        self.entity_uuid = entity_uuid
        # The UUID of the event.
        self.event_uuid = event_uuid
        self.execute_uuid = execute_uuid
        # The field used to sort the results.
        # 
        # > You can obtain the sort field from the response of this operation.
        self.order_field = order_field
        # The page number of the page to return. Default value: 1, which indicates the first page.
        self.page_number = page_number
        # The maximum number of entries to return on each page for paging queries. Default value: 20. If the PageSize parameter is left empty, 10 entries are returned by default.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The fuzzy match content. This parameter queries the entity, disposal scene, and disposal parameter fields.
        self.param_content = param_content
        # The end time of the query range for the disposal time. Format: 13-digit timestamp.
        self.process_action_end = process_action_end
        # The start time of the query range for the disposal time. Format: 13-digit timestamp.
        self.process_action_start = process_action_start
        # The end time of the query range for the unblocking time. Format: 13-digit timestamp.
        self.process_remove_end = process_remove_end
        # The start time of the query range for the unblocking time. Format: 13-digit timestamp.
        self.process_remove_start = process_remove_start
        # The UUID of the disposal strategy.
        # >You can call the [ListDisposeStrategy](https://help.aliyun.com/document_detail/2584440.html) operation to obtain this parameter.
        self.process_strategy_uuid = process_strategy_uuid
        # The trigger ID of the playbook.
        self.req_uuid = req_uuid
        self.response_rule_id = response_rule_id
        # The scene code of the disposal task.
        # >You can call the [DescribeEnumItems](~~DescribeEnumItems~~) operation to obtain this parameter.
        self.scene_code = scene_code
        # The Alibaba Cloud account ID for the disposal.
        self.scope = scope
        # The trigger source of the disposal task, in array string format. Valid values:
        # 
        # - **system**: Triggered by manual event disposal.
        # - **custom**: Triggered by an automatic response rule based on an event.
        # - **custom_alert**: Triggered by an automatic response rule based on an alert.
        # - **soar-manual**: Triggered by manually invoking a SOAR playbook.
        # - **soar-mdr**: Triggered by the Managed Security Service.
        self.source = source
        # The unique identifier of the disposal task.
        # 
        # > This parameter is used to query a specific task. You can obtain the value from the response of this operation.
        self.task_id = task_id
        # The status list of the disposal task, in data string format. Valid values:
        # 
        # - **11**: Disposing.
        # - **21**: Blocking.
        # - **22**: Isolating.
        # - **23**: Ended.
        # - **24**: Whitelisted.
        # - **20**: Succeeded.
        # - **90**: Failed.
        # - **91**: Unblocking failed.
        # - **92**: Unisolation failed.
        self.task_status = task_status
        # The trigger source of the disposal task. Valid values:
        # 
        # - **system**: Triggered by manual event disposal.
        # - **custom**: Triggered by an automatic response rule based on an event.
        # - **custom_alert**: Triggered by an automatic response rule based on an alert.
        # - **soar-manual**: Triggered by manually invoking a SOAR playbook.
        # - **soar-mdr**: Triggered by the Managed Security Service.
        self.trigger_source = trigger_source
        # The cloud product associated with the disposal task, in data string format. Valid values:
        # 
        # - **WAF**: Web Application Firewall.
        # - **CFW**: Cloud Firewall.
        # - **Aegis**: Security Center.
        self.yun_code = yun_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.event_uuid is not None:
            result['EventUuid'] = self.event_uuid

        if self.execute_uuid is not None:
            result['ExecuteUuid'] = self.execute_uuid

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.param_content is not None:
            result['ParamContent'] = self.param_content

        if self.process_action_end is not None:
            result['ProcessActionEnd'] = self.process_action_end

        if self.process_action_start is not None:
            result['ProcessActionStart'] = self.process_action_start

        if self.process_remove_end is not None:
            result['ProcessRemoveEnd'] = self.process_remove_end

        if self.process_remove_start is not None:
            result['ProcessRemoveStart'] = self.process_remove_start

        if self.process_strategy_uuid is not None:
            result['ProcessStrategyUuid'] = self.process_strategy_uuid

        if self.req_uuid is not None:
            result['ReqUuid'] = self.req_uuid

        if self.response_rule_id is not None:
            result['ResponseRuleId'] = self.response_rule_id

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.source is not None:
            result['Source'] = self.source

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.yun_code is not None:
            result['YunCode'] = self.yun_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('EventUuid') is not None:
            self.event_uuid = m.get('EventUuid')

        if m.get('ExecuteUuid') is not None:
            self.execute_uuid = m.get('ExecuteUuid')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParamContent') is not None:
            self.param_content = m.get('ParamContent')

        if m.get('ProcessActionEnd') is not None:
            self.process_action_end = m.get('ProcessActionEnd')

        if m.get('ProcessActionStart') is not None:
            self.process_action_start = m.get('ProcessActionStart')

        if m.get('ProcessRemoveEnd') is not None:
            self.process_remove_end = m.get('ProcessRemoveEnd')

        if m.get('ProcessRemoveStart') is not None:
            self.process_remove_start = m.get('ProcessRemoveStart')

        if m.get('ProcessStrategyUuid') is not None:
            self.process_strategy_uuid = m.get('ProcessStrategyUuid')

        if m.get('ReqUuid') is not None:
            self.req_uuid = m.get('ReqUuid')

        if m.get('ResponseRuleId') is not None:
            self.response_rule_id = m.get('ResponseRuleId')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('YunCode') is not None:
            self.yun_code = m.get('YunCode')

        return self

