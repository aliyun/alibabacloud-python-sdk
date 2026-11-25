# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProjectInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeProjectInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeProjectInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeProjectInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_step_no: int = None,
        customer_ali_uid: int = None,
        final_step_no: int = None,
        finish_type: str = None,
        gmt_create: int = None,
        gmt_expired: int = None,
        gmt_finished: int = None,
        instance_id: str = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_sku_name: str = None,
        project_status: str = None,
        supplier_ali_uid: int = None,
        template_id: int = None,
        template_type: str = None,
    ):
        # The current step in the process.
        self.current_step_no = current_step_no
        # The Alibaba Cloud UID of the customer.
        self.customer_ali_uid = customer_ali_uid
        # The sequence number of the last step.
        self.final_step_no = final_step_no
        # The completion method of the project. Valid values:
        # 
        # - null: The default value for unfinished projects.
        # - CustomerConfirm: Manually confirmed by the customer.
        # - SystemAutoConfirm: Automatically confirmed by the system due to timeout.
        self.finish_type = finish_type
        # The creation time of the project. The value is a UNIX timestamp.
        self.gmt_create = gmt_create
        # The expiration time of the project. The value is a UNIX timestamp.
        self.gmt_expired = gmt_expired
        # The completion time of the project. The value is a UNIX timestamp.
        self.gmt_finished = gmt_finished
        # The business instance ID in Cloud Marketplace.
        self.instance_id = instance_id
        # The order ID.
        self.order_id = order_id
        # The product code.
        self.product_code = product_code
        # The name of the Cloud Marketplace product.
        self.product_name = product_name
        # The code of the Cloud Marketplace product SKU.
        self.product_sku_code = product_sku_code
        # The name of the Cloud Marketplace product SKU.
        self.product_sku_name = product_sku_name
        # The execution status of the project. Valid values:
        # 
        # - Starting: In progress.
        # - Cancel: Canceled.
        # - Pause: Paused.
        # - Finish: Completed.
        self.project_status = project_status
        # The UID of the supplier to which the project belongs.
        self.supplier_ali_uid = supplier_ali_uid
        # The ID of the process template to which the project belongs.
        self.template_id = template_id
        # The template type of the project. Valid values:
        # 
        # - Public: Public template.
        # - Private: Private template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_step_no is not None:
            result['CurrentStepNo'] = self.current_step_no

        if self.customer_ali_uid is not None:
            result['CustomerAliUid'] = self.customer_ali_uid

        if self.final_step_no is not None:
            result['FinalStepNo'] = self.final_step_no

        if self.finish_type is not None:
            result['FinishType'] = self.finish_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_finished is not None:
            result['GmtFinished'] = self.gmt_finished

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code

        if self.product_sku_name is not None:
            result['ProductSkuName'] = self.product_sku_name

        if self.project_status is not None:
            result['ProjectStatus'] = self.project_status

        if self.supplier_ali_uid is not None:
            result['SupplierAliUid'] = self.supplier_ali_uid

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentStepNo') is not None:
            self.current_step_no = m.get('CurrentStepNo')

        if m.get('CustomerAliUid') is not None:
            self.customer_ali_uid = m.get('CustomerAliUid')

        if m.get('FinalStepNo') is not None:
            self.final_step_no = m.get('FinalStepNo')

        if m.get('FinishType') is not None:
            self.finish_type = m.get('FinishType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtFinished') is not None:
            self.gmt_finished = m.get('GmtFinished')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')

        if m.get('ProductSkuName') is not None:
            self.product_sku_name = m.get('ProductSkuName')

        if m.get('ProjectStatus') is not None:
            self.project_status = m.get('ProjectStatus')

        if m.get('SupplierAliUid') is not None:
            self.supplier_ali_uid = m.get('SupplierAliUid')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

