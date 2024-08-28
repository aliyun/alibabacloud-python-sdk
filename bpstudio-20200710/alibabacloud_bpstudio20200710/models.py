# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class BillingApplicationRequest(TeaModel):
    def __init__(
        self,
        month: int = None,
        resource_group_id: str = None,
        year: int = None,
    ):
        self.month = month
        self.resource_group_id = resource_group_id
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.month is not None:
            result['Month'] = self.month
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class BillingApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BillingApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BillingApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BillingApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeployDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        max_results: int = None,
        next_token: int = None,
        ref_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        self.ref_id = ref_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.ref_id is not None:
            result['RefId'] = self.ref_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RefId') is not None:
            self.ref_id = m.get('RefId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetDeployDetailResponseBodyDataResourceListOperation(TeaModel):
    def __init__(
        self,
        name: str = None,
        operations: Dict[str, Any] = None,
    ):
        self.name = name
        self.operations = operations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.operations is not None:
            result['Operations'] = self.operations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        return self


class GetDeployDetailResponseBodyDataResourceListResourceTimeList(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        creation_end_time: int = None,
        creation_start_time: int = None,
        id: int = None,
    ):
        self.biz_id = biz_id
        self.creation_end_time = creation_end_time
        self.creation_start_time = creation_start_time
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.creation_end_time is not None:
            result['CreationEndTime'] = self.creation_end_time
        if self.creation_start_time is not None:
            result['CreationStartTime'] = self.creation_start_time
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CreationEndTime') is not None:
            self.creation_end_time = m.get('CreationEndTime')
        if m.get('CreationStartTime') is not None:
            self.creation_start_time = m.get('CreationStartTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class GetDeployDetailResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        buy_duration: str = None,
        charge_type: str = None,
        execution_strategy: str = None,
        modified_time: int = None,
        monitor_url: str = None,
        node_name: str = None,
        operation: GetDeployDetailResponseBodyDataResourceListOperation = None,
        ref_id: int = None,
        remark: str = None,
        resource_code: str = None,
        resource_id: str = None,
        resource_time_list: List[GetDeployDetailResponseBodyDataResourceListResourceTimeList] = None,
        resource_type: str = None,
        status: str = None,
    ):
        self.buy_duration = buy_duration
        self.charge_type = charge_type
        self.execution_strategy = execution_strategy
        self.modified_time = modified_time
        self.monitor_url = monitor_url
        self.node_name = node_name
        self.operation = operation
        self.ref_id = ref_id
        self.remark = remark
        self.resource_code = resource_code
        self.resource_id = resource_id
        self.resource_time_list = resource_time_list
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        if self.operation:
            self.operation.validate()
        if self.resource_time_list:
            for k in self.resource_time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_duration is not None:
            result['BuyDuration'] = self.buy_duration
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.execution_strategy is not None:
            result['ExecutionStrategy'] = self.execution_strategy
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.monitor_url is not None:
            result['MonitorURL'] = self.monitor_url
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.operation is not None:
            result['Operation'] = self.operation.to_map()
        if self.ref_id is not None:
            result['RefId'] = self.ref_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['ResourceTimeList'] = []
        if self.resource_time_list is not None:
            for k in self.resource_time_list:
                result['ResourceTimeList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyDuration') is not None:
            self.buy_duration = m.get('BuyDuration')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExecutionStrategy') is not None:
            self.execution_strategy = m.get('ExecutionStrategy')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('MonitorURL') is not None:
            self.monitor_url = m.get('MonitorURL')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Operation') is not None:
            temp_model = GetDeployDetailResponseBodyDataResourceListOperation()
            self.operation = temp_model.from_map(m['Operation'])
        if m.get('RefId') is not None:
            self.ref_id = m.get('RefId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.resource_time_list = []
        if m.get('ResourceTimeList') is not None:
            for k in m.get('ResourceTimeList'):
                temp_model = GetDeployDetailResponseBodyDataResourceListResourceTimeList()
                self.resource_time_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeployDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        current_process: str = None,
        deleting_node_list: List[Dict[str, Any]] = None,
        deploy_percent: float = None,
        deployed_node_list: List[Dict[str, Any]] = None,
        deploying_node_list: List[Dict[str, Any]] = None,
        error: str = None,
        execution_time: int = None,
        fail_status: int = None,
        order_id_list: List[str] = None,
        pdf_url: str = None,
        resource_group_id: str = None,
        resource_list: List[GetDeployDetailResponseBodyDataResourceList] = None,
        status: str = None,
        terraform_script_url: str = None,
    ):
        self.app_id = app_id
        self.create_time = create_time
        self.current_process = current_process
        self.deleting_node_list = deleting_node_list
        self.deploy_percent = deploy_percent
        self.deployed_node_list = deployed_node_list
        self.deploying_node_list = deploying_node_list
        self.error = error
        self.execution_time = execution_time
        self.fail_status = fail_status
        self.order_id_list = order_id_list
        self.pdf_url = pdf_url
        self.resource_group_id = resource_group_id
        self.resource_list = resource_list
        self.status = status
        self.terraform_script_url = terraform_script_url

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_process is not None:
            result['CurrentProcess'] = self.current_process
        if self.deleting_node_list is not None:
            result['DeletingNodeList'] = self.deleting_node_list
        if self.deploy_percent is not None:
            result['DeployPercent'] = self.deploy_percent
        if self.deployed_node_list is not None:
            result['DeployedNodeList'] = self.deployed_node_list
        if self.deploying_node_list is not None:
            result['DeployingNodeList'] = self.deploying_node_list
        if self.error is not None:
            result['Error'] = self.error
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.fail_status is not None:
            result['FailStatus'] = self.fail_status
        if self.order_id_list is not None:
            result['OrderIdList'] = self.order_id_list
        if self.pdf_url is not None:
            result['PdfUrl'] = self.pdf_url
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.terraform_script_url is not None:
            result['TerraformScriptUrl'] = self.terraform_script_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentProcess') is not None:
            self.current_process = m.get('CurrentProcess')
        if m.get('DeletingNodeList') is not None:
            self.deleting_node_list = m.get('DeletingNodeList')
        if m.get('DeployPercent') is not None:
            self.deploy_percent = m.get('DeployPercent')
        if m.get('DeployedNodeList') is not None:
            self.deployed_node_list = m.get('DeployedNodeList')
        if m.get('DeployingNodeList') is not None:
            self.deploying_node_list = m.get('DeployingNodeList')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('FailStatus') is not None:
            self.fail_status = m.get('FailStatus')
        if m.get('OrderIdList') is not None:
            self.order_id_list = m.get('OrderIdList')
        if m.get('PdfUrl') is not None:
            self.pdf_url = m.get('PdfUrl')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = GetDeployDetailResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TerraformScriptUrl') is not None:
            self.terraform_script_url = m.get('TerraformScriptUrl')
        return self


class GetDeployDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetDeployDetailResponseBodyData] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDeployDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetDeployDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeployDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeployDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


