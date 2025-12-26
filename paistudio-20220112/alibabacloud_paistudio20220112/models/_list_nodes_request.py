# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        accelerator_type: str = None,
        availability_zone: str = None,
        clique_id: str = None,
        filter_by_quota_id: str = None,
        filter_by_resource_group_ids: str = None,
        gputype: str = None,
        health_count: main_models.ListNodesRequestHealthCount = None,
        health_rate: main_models.ListNodesRequestHealthRate = None,
        hyper_node: str = None,
        hyper_zone: str = None,
        layout_mode: str = None,
        machine_group_ids: str = None,
        node_names: str = None,
        node_statuses: str = None,
        node_types: str = None,
        order: str = None,
        order_instance_ids: str = None,
        order_statuses: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        quota_id: str = None,
        reason_codes: str = None,
        resource_group_ids: str = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        self.accelerator_type = accelerator_type
        self.availability_zone = availability_zone
        self.clique_id = clique_id
        self.filter_by_quota_id = filter_by_quota_id
        self.filter_by_resource_group_ids = filter_by_resource_group_ids
        self.gputype = gputype
        self.health_count = health_count
        self.health_rate = health_rate
        self.hyper_node = hyper_node
        self.hyper_zone = hyper_zone
        self.layout_mode = layout_mode
        self.machine_group_ids = machine_group_ids
        self.node_names = node_names
        self.node_statuses = node_statuses
        self.node_types = node_types
        self.order = order
        self.order_instance_ids = order_instance_ids
        self.order_statuses = order_statuses
        self.page_number = page_number
        self.page_size = page_size
        self.payment_type = payment_type
        self.quota_id = quota_id
        self.reason_codes = reason_codes
        self.resource_group_ids = resource_group_ids
        self.sort_by = sort_by
        self.verbose = verbose
        self.workspace_id = workspace_id

    def validate(self):
        if self.health_count:
            self.health_count.validate()
        if self.health_rate:
            self.health_rate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_type is not None:
            result['AcceleratorType'] = self.accelerator_type

        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.clique_id is not None:
            result['CliqueID'] = self.clique_id

        if self.filter_by_quota_id is not None:
            result['FilterByQuotaId'] = self.filter_by_quota_id

        if self.filter_by_resource_group_ids is not None:
            result['FilterByResourceGroupIds'] = self.filter_by_resource_group_ids

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.health_count is not None:
            result['HealthCount'] = self.health_count.to_map()

        if self.health_rate is not None:
            result['HealthRate'] = self.health_rate.to_map()

        if self.hyper_node is not None:
            result['HyperNode'] = self.hyper_node

        if self.hyper_zone is not None:
            result['HyperZone'] = self.hyper_zone

        if self.layout_mode is not None:
            result['LayoutMode'] = self.layout_mode

        if self.machine_group_ids is not None:
            result['MachineGroupIds'] = self.machine_group_ids

        if self.node_names is not None:
            result['NodeNames'] = self.node_names

        if self.node_statuses is not None:
            result['NodeStatuses'] = self.node_statuses

        if self.node_types is not None:
            result['NodeTypes'] = self.node_types

        if self.order is not None:
            result['Order'] = self.order

        if self.order_instance_ids is not None:
            result['OrderInstanceIds'] = self.order_instance_ids

        if self.order_statuses is not None:
            result['OrderStatuses'] = self.order_statuses

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.reason_codes is not None:
            result['ReasonCodes'] = self.reason_codes

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorType') is not None:
            self.accelerator_type = m.get('AcceleratorType')

        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('CliqueID') is not None:
            self.clique_id = m.get('CliqueID')

        if m.get('FilterByQuotaId') is not None:
            self.filter_by_quota_id = m.get('FilterByQuotaId')

        if m.get('FilterByResourceGroupIds') is not None:
            self.filter_by_resource_group_ids = m.get('FilterByResourceGroupIds')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('HealthCount') is not None:
            temp_model = main_models.ListNodesRequestHealthCount()
            self.health_count = temp_model.from_map(m.get('HealthCount'))

        if m.get('HealthRate') is not None:
            temp_model = main_models.ListNodesRequestHealthRate()
            self.health_rate = temp_model.from_map(m.get('HealthRate'))

        if m.get('HyperNode') is not None:
            self.hyper_node = m.get('HyperNode')

        if m.get('HyperZone') is not None:
            self.hyper_zone = m.get('HyperZone')

        if m.get('LayoutMode') is not None:
            self.layout_mode = m.get('LayoutMode')

        if m.get('MachineGroupIds') is not None:
            self.machine_group_ids = m.get('MachineGroupIds')

        if m.get('NodeNames') is not None:
            self.node_names = m.get('NodeNames')

        if m.get('NodeStatuses') is not None:
            self.node_statuses = m.get('NodeStatuses')

        if m.get('NodeTypes') is not None:
            self.node_types = m.get('NodeTypes')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderInstanceIds') is not None:
            self.order_instance_ids = m.get('OrderInstanceIds')

        if m.get('OrderStatuses') is not None:
            self.order_statuses = m.get('OrderStatuses')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('ReasonCodes') is not None:
            self.reason_codes = m.get('ReasonCodes')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListNodesRequestHealthRate(DaraModel):
    def __init__(
        self,
        operation: str = None,
        value: int = None,
    ):
        self.operation = operation
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['operation'] = self.operation

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListNodesRequestHealthCount(DaraModel):
    def __init__(
        self,
        operation: str = None,
        value: int = None,
    ):
        self.operation = operation
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['operation'] = self.operation

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

