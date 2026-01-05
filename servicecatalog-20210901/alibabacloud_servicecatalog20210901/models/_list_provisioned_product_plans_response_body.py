# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProvisionedProductPlansResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan_details: List[main_models.ListProvisionedProductPlansResponseBodyPlanDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # An array that consists of plans.
        self.plan_details = plan_details
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.plan_details:
            for v1 in self.plan_details:
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

        result['PlanDetails'] = []
        if self.plan_details is not None:
            for k1 in self.plan_details:
                result['PlanDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.plan_details = []
        if m.get('PlanDetails') is not None:
            for k1 in m.get('PlanDetails'):
                temp_model = main_models.ListProvisionedProductPlansResponseBodyPlanDetails()
                self.plan_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProvisionedProductPlansResponseBodyPlanDetails(DaraModel):
    def __init__(
        self,
        assigned_approvers: List[main_models.ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers] = None,
        create_time: str = None,
        description: str = None,
        operation_type: str = None,
        owner_principal_id: str = None,
        owner_principal_name: str = None,
        owner_principal_type: str = None,
        parameters: List[main_models.ListProvisionedProductPlansResponseBodyPlanDetailsParameters] = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        stack_id: str = None,
        stack_region_id: str = None,
        status: str = None,
        status_message: str = None,
        tags: List[main_models.ListProvisionedProductPlansResponseBodyPlanDetailsTags] = None,
        uid: str = None,
        update_time: str = None,
    ):
        # An array that consists of reviewers.
        self.assigned_approvers = assigned_approvers
        # The time when the plan was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the plan.
        self.description = description
        # The purpose of the plan. Valid values:
        # 
        # *   LaunchProduct: launches the product. This is the default value.
        # *   UpdateProvisionedProduct: updates the information about the product instance.
        # *   TerminateProvisionedProduct: terminates the product instance.
        self.operation_type = operation_type
        # The ID of the RAM entity to which the plan belongs.
        self.owner_principal_id = owner_principal_id
        # The name of the RAM entity to which the plan belongs.
        self.owner_principal_name = owner_principal_name
        # The type of the RAM entity to which the plan belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type
        # An array that consists of the parameters in the template.
        self.parameters = parameters
        # The ID of the plan.
        self.plan_id = plan_id
        # The name of the plan.
        self.plan_name = plan_name
        # The type of the plan.
        # 
        # The value is fixed as Ros, which indicates Resource Orchestration Service (ROS).
        self.plan_type = plan_type
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id
        # The ID of the product.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name
        # The ID of the ROS stack.
        self.stack_id = stack_id
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id
        # The state of the plan. Valid values:
        # 
        # *   PreviewInProgress: The plan is being prechecked.
        # *   PreviewSuccess: The precheck is successful.
        # *   PreviewFailed: The precheck fails.
        # *   ApplicationInProgress: The plan is being reviewed.
        # *   ApplicationApproved: The plan is approved.
        # *   ApplicationRejected: The approval is rejected.
        # *   ExecuteInProgress: The plan is being run.
        # *   ExecuteSuccess: The plan is run.
        # *   ExecuteFailed: The plan fails to be run.
        # *   Canceled: The plan is canceled.
        self.status = status
        # The message returned for the state.
        # 
        # > This parameter is returned only when PreviewFailed or ExecuteFailed is returned for the Status parameter.
        self.status_message = status_message
        # An array that consists of custom tags.
        self.tags = tags
        # The ID of the Alibaba Cloud account to which the plan belongs.
        self.uid = uid
        # The last time when the task was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.assigned_approvers:
            for v1 in self.assigned_approvers:
                 if v1:
                    v1.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignedApprovers'] = []
        if self.assigned_approvers is not None:
            for k1 in self.assigned_approvers:
                result['AssignedApprovers'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id

        if self.owner_principal_name is not None:
            result['OwnerPrincipalName'] = self.owner_principal_name

        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.plan_type is not None:
            result['PlanType'] = self.plan_type

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assigned_approvers = []
        if m.get('AssignedApprovers') is not None:
            for k1 in m.get('AssignedApprovers'):
                temp_model = main_models.ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers()
                self.assigned_approvers.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')

        if m.get('OwnerPrincipalName') is not None:
            self.owner_principal_name = m.get('OwnerPrincipalName')

        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.ListProvisionedProductPlansResponseBodyPlanDetailsParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListProvisionedProductPlansResponseBodyPlanDetailsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListProvisionedProductPlansResponseBodyPlanDetailsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the custom tag.
        self.key = key
        # The value of the custom tag.
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

class ListProvisionedProductPlansResponseBodyPlanDetailsParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter in the template.
        self.parameter_key = parameter_key
        # The value of the parameter in the template.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class ListProvisionedProductPlansResponseBodyPlanDetailsAssignedApprovers(DaraModel):
    def __init__(
        self,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The RAM entity name of the reviewer.
        self.principal_name = principal_name
        # The type of the RAM entity of the reviewer. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

