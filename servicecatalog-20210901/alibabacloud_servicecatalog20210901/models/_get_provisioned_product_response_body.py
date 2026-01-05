# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class GetProvisionedProductResponseBody(DaraModel):
    def __init__(
        self,
        provisioned_product_detail: main_models.GetProvisionedProductResponseBodyProvisionedProductDetail = None,
        request_id: str = None,
    ):
        # The details of the product instance.
        self.provisioned_product_detail = provisioned_product_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.provisioned_product_detail:
            self.provisioned_product_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provisioned_product_detail is not None:
            result['ProvisionedProductDetail'] = self.provisioned_product_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductDetail') is not None:
            temp_model = main_models.GetProvisionedProductResponseBodyProvisionedProductDetail()
            self.provisioned_product_detail = temp_model.from_map(m.get('ProvisionedProductDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProvisionedProductResponseBodyProvisionedProductDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        last_provisioning_task_id: str = None,
        last_successful_provisioning_task_id: str = None,
        last_task_id: str = None,
        owner_principal_id: str = None,
        owner_principal_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_arn: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        provisioned_product_type: str = None,
        stack_id: str = None,
        stack_region_id: str = None,
        status: str = None,
        status_message: str = None,
    ):
        # The time when the product instance was created.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the task that was last run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_provisioning_task_id = last_provisioning_task_id
        # The ID of the last task that was successfully run on the product instance.
        # 
        # The task can be one of the following types:
        # 
        # *   LaunchProduct: a task that launches the product.
        # *   UpdateProvisionedProduct: a task that updates the information about the product instance.
        # *   TerminateProvisionedProduct: a task that terminates the product instance.
        self.last_successful_provisioning_task_id = last_successful_provisioning_task_id
        # The ID of the task that was last run.
        self.last_task_id = last_task_id
        # The ID of the RAM entity to which the product instance belongs.
        self.owner_principal_id = owner_principal_id
        # The type of the Resource Access Management (RAM) entity to which the product instance belongs. Valid values:
        # 
        # *   RamUser: a RAM user
        # *   RamRole: a RAM role
        self.owner_principal_type = owner_principal_type
        # The ID of the product portfolio.
        self.portfolio_id = portfolio_id
        # The ID of the product.
        self.product_id = product_id
        # The name of the product.
        self.product_name = product_name
        # The ID of the product version.
        self.product_version_id = product_version_id
        # The name of the product version.
        self.product_version_name = product_version_name
        # The Alibaba Cloud Resource Name (ARN) of the product instance.
        self.provisioned_product_arn = provisioned_product_arn
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id
        # The name of the product instance.
        self.provisioned_product_name = provisioned_product_name
        # The type of the product instance.
        # 
        # The value is fixed as RosStack, which indicates an ROS stack.
        self.provisioned_product_type = provisioned_product_type
        # The ID of the Resource Orchestration Service (ROS) stack.
        self.stack_id = stack_id
        # The ID of the region to which the ROS stack belongs.
        self.stack_region_id = stack_region_id
        # The state of the product instance. Valid values:
        # 
        # *   Available: The product instance was available.
        # *   UnderChange: The information about the product instance was being changed.
        # *   Error: An exception occurred on the product instance.
        self.status = status
        # The message that is returned for the status of the product instance.
        # 
        # > This parameter is returned only when Error is returned for the Status parameter.
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_provisioning_task_id is not None:
            result['LastProvisioningTaskId'] = self.last_provisioning_task_id

        if self.last_successful_provisioning_task_id is not None:
            result['LastSuccessfulProvisioningTaskId'] = self.last_successful_provisioning_task_id

        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id

        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id

        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type

        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        if self.provisioned_product_arn is not None:
            result['ProvisionedProductArn'] = self.provisioned_product_arn

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name

        if self.provisioned_product_type is not None:
            result['ProvisionedProductType'] = self.provisioned_product_type

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastProvisioningTaskId') is not None:
            self.last_provisioning_task_id = m.get('LastProvisioningTaskId')

        if m.get('LastSuccessfulProvisioningTaskId') is not None:
            self.last_successful_provisioning_task_id = m.get('LastSuccessfulProvisioningTaskId')

        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')

        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')

        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')

        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        if m.get('ProvisionedProductArn') is not None:
            self.provisioned_product_arn = m.get('ProvisionedProductArn')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')

        if m.get('ProvisionedProductType') is not None:
            self.provisioned_product_type = m.get('ProvisionedProductType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        return self

