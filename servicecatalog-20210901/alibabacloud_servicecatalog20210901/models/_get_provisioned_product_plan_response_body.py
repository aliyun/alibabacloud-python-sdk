# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetProvisionedProductPlanResponseBody(DaraModel):
    def __init__(
        self,
        plan_detail: main_models.GetProvisionedProductPlanResponseBodyPlanDetail = None,
        product_detail: main_models.GetProvisionedProductPlanResponseBodyProductDetail = None,
        product_version_detail: main_models.GetProvisionedProductPlanResponseBodyProductVersionDetail = None,
        request_id: str = None,
        resource_changes: List[main_models.GetProvisionedProductPlanResponseBodyResourceChanges] = None,
    ):
        # The details of the plan.
        self.plan_detail = plan_detail
        # The details of the product.
        self.product_detail = product_detail
        # The details of the product version.
        self.product_version_detail = product_version_detail
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the resources to be changed in the plan.
        self.resource_changes = resource_changes

    def validate(self):
        if self.plan_detail:
            self.plan_detail.validate()
        if self.product_detail:
            self.product_detail.validate()
        if self.product_version_detail:
            self.product_version_detail.validate()
        if self.resource_changes:
            for v1 in self.resource_changes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plan_detail is not None:
            result['PlanDetail'] = self.plan_detail.to_map()

        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail.to_map()

        if self.product_version_detail is not None:
            result['ProductVersionDetail'] = self.product_version_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceChanges'] = []
        if self.resource_changes is not None:
            for k1 in self.resource_changes:
                result['ResourceChanges'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanDetail') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetail()
            self.plan_detail = temp_model.from_map(m.get('PlanDetail'))

        if m.get('ProductDetail') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyProductDetail()
            self.product_detail = temp_model.from_map(m.get('ProductDetail'))

        if m.get('ProductVersionDetail') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyProductVersionDetail()
            self.product_version_detail = temp_model.from_map(m.get('ProductVersionDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_changes = []
        if m.get('ResourceChanges') is not None:
            for k1 in m.get('ResourceChanges'):
                temp_model = main_models.GetProvisionedProductPlanResponseBodyResourceChanges()
                self.resource_changes.append(temp_model.from_map(k1))

        return self

class GetProvisionedProductPlanResponseBodyResourceChanges(DaraModel):
    def __init__(
        self,
        action: str = None,
        logical_resource_id: str = None,
        physical_resource_id: str = None,
        replacement: str = None,
        resource_type: str = None,
    ):
        # The action that is performed on the resource. Valid values:
        # 
        # *   Add
        # *   Modify
        # *   Remove
        # *   None
        self.action = action
        # The logical ID of the resource.
        self.logical_resource_id = logical_resource_id
        # The physical ID of the resource.
        # 
        # >  This parameter is returned if the value of Action is Modify or Remove.
        self.physical_resource_id = physical_resource_id
        # Indicates whether a replacement update is performed on the template. Valid values:
        # 
        # *   True: A replacement update is performed on the template.
        # *   False: A change is made on the template.
        # *   Conditional: A replacement update may be performed on the template. You can check whether a replacement update is performed when the template is in use.
        # 
        # >  This parameter is returned if the value of Action is Modify.
        self.replacement = replacement
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.physical_resource_id is not None:
            result['PhysicalResourceId'] = self.physical_resource_id

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('PhysicalResourceId') is not None:
            self.physical_resource_id = m.get('PhysicalResourceId')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class GetProvisionedProductPlanResponseBodyProductVersionDetail(DaraModel):
    def __init__(
        self,
        active: bool = None,
        create_time: str = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # Indicates whether the product version is visible to end users. Valid values:
        # 
        # *   true (default)
        # *   false
        self.active = active
        # The time when the product version was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product version.
        self.description = description
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommendation version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be deprecated.
        self.guidance = guidance
        # The ID of the product to which the product version belongs.
        self.product_id = product_id
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The name for the version of the product.
        self.product_version_name = product_version_name
        # The type of the template.
        # 
        # The value is fixed as RosTerraformTemplate, which indicates that the Terraform template is supported by ROS.
        self.template_type = template_type
        # The URL of the template.
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.guidance is not None:
            result['Guidance'] = self.guidance

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')

        return self

class GetProvisionedProductPlanResponseBodyProductDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
    ):
        # The creation time.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the product.
        self.description = description
        # The Alibaba Cloud Resource Name (ARN) of the product.
        self.product_arn = product_arn
        # The ID of the product.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The type of the product.
        # 
        # The value is fixed as Ros, which indicates ROS.
        self.product_type = product_type
        # The provider of the product.
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

class GetProvisionedProductPlanResponseBodyPlanDetail(DaraModel):
    def __init__(
        self,
        approval_detail: main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail = None,
        assigned_approvers: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers] = None,
        create_time: str = None,
        description: str = None,
        operation_type: str = None,
        owner_principal_id: str = None,
        owner_principal_name: str = None,
        owner_principal_type: str = None,
        parameters: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailParameters] = None,
        plan_id: str = None,
        plan_name: str = None,
        plan_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        stack_id: str = None,
        stack_region_id: str = None,
        status: str = None,
        status_message: str = None,
        tags: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailTags] = None,
        uid: str = None,
        update_time: str = None,
    ):
        # The approval details of the plan.
        self.approval_detail = approval_detail
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
        # *   LaunchProduct: launches the product.
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
        # *   ApplicationInProgress: The plan is being approved.
        # *   ApplicationApproved: The plan is approved.
        # *   ApplicationRejected: The approval is rejected.
        # *   ExecuteInProgress: The plan is being run.
        # *   ExecuteSuccess: The plan is run.
        # *   ExecuteFailed: The plan fails to be run.
        # *   Canceled: The plan is canceled.
        self.status = status
        # The message returned for the state.
        # 
        # > This parameter is returned only when PreviewFailed or ExecuteFailed is returned for Status.
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
        if self.approval_detail:
            self.approval_detail.validate()
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
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail.to_map()

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
        if m.get('ApprovalDetail') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail()
            self.approval_detail = temp_model.from_map(m.get('ApprovalDetail'))

        self.assigned_approvers = []
        if m.get('AssignedApprovers') is not None:
            for k1 in m.get('AssignedApprovers'):
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers()
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
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailParameters()
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
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetProvisionedProductPlanResponseBodyPlanDetailTags(DaraModel):
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

class GetProvisionedProductPlanResponseBodyPlanDetailParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the input parameter for the template.
        self.parameter_key = parameter_key
        # The value of the input parameter for the template.
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

class GetProvisionedProductPlanResponseBodyPlanDetailAssignedApprovers(DaraModel):
    def __init__(
        self,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The name of the RAM entity of the plan approver.
        self.principal_name = principal_name
        # The type of the Resource Access Management (RAM) entity of the plan approver. Valid values:
        # 
        # *   RamUser: a RAM user.
        # *   RamRole: a RAM role.
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

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetail(DaraModel):
    def __init__(
        self,
        operation_records: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords] = None,
        todo_task_activities: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities] = None,
    ):
        # The operation records.
        self.operation_records = operation_records
        # The operations that are being performed by the plan.
        self.todo_task_activities = todo_task_activities

    def validate(self):
        if self.operation_records:
            for v1 in self.operation_records:
                 if v1:
                    v1.validate()
        if self.todo_task_activities:
            for v1 in self.todo_task_activities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationRecords'] = []
        if self.operation_records is not None:
            for k1 in self.operation_records:
                result['OperationRecords'].append(k1.to_map() if k1 else None)

        result['TodoTaskActivities'] = []
        if self.todo_task_activities is not None:
            for k1 in self.todo_task_activities:
                result['TodoTaskActivities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_records = []
        if m.get('OperationRecords') is not None:
            for k1 in m.get('OperationRecords'):
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords()
                self.operation_records.append(temp_model.from_map(k1))

        self.todo_task_activities = []
        if m.get('TodoTaskActivities') is not None:
            for k1 in m.get('TodoTaskActivities'):
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities()
                self.todo_task_activities.append(temp_model.from_map(k1))

        return self

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivities(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        tasks: List[main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks] = None,
    ):
        # The name of the operation that is being performed by the plan.
        self.activity_name = activity_name
        # The tasks that are pending for review.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasks(DaraModel):
    def __init__(
        self,
        operator: main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator = None,
    ):
        # The RAM entities that can perform operations on the plan.
        self.operator = operator

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['Operator'] = self.operator.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator()
            self.operator = temp_model.from_map(m.get('Operator'))

        return self

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailTodoTaskActivitiesTasksOperator(DaraModel):
    def __init__(
        self,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The name of the RAM entity.
        self.principal_name = principal_name
        # The type of the RAM entity. Valid values:
        # 
        # *   RamUser: a RAM user.
        # *   RamRole: a RAM role.
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

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecords(DaraModel):
    def __init__(
        self,
        approval_action: str = None,
        comment: str = None,
        create_time: str = None,
        operator: main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator = None,
    ):
        # The operation that is performed by the operator on the plan. Valid values:
        # 
        # *   Submit: submits the plan.
        # *   Cancel: cancels the plan.
        # *   Approve: approves the plan.
        # *   reject: rejectes the plan.
        self.approval_action = approval_action
        # The approval comment of the operator.
        self.comment = comment
        # The time when the operation was performed.
        self.create_time = create_time
        # The RAM entities that have performed operations on the plan.
        self.operator = operator

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.operator is not None:
            result['Operator'] = self.operator.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Operator') is not None:
            temp_model = main_models.GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator()
            self.operator = temp_model.from_map(m.get('Operator'))

        return self

class GetProvisionedProductPlanResponseBodyPlanDetailApprovalDetailOperationRecordsOperator(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The ID of the RAM entity.
        self.principal_id = principal_id
        # The name RAM entity that servers as the operator.
        self.principal_name = principal_name
        # The type of the RAM entity. Valid values:
        # 
        # *   RamUser: a RAM user.
        # *   RamRole: a RAM role.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

