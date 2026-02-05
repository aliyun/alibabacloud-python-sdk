# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from alibabacloud_customerservice20231228 import models as main_models
from darabonba.model import DaraModel

class ListServiceApplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListServiceApplyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListServiceApplyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListServiceApplyResponseBodyData(DaraModel):
    def __init__(
        self,
        extend: Any = None,
        list: List[main_models.ListServiceApplyResponseBodyDataList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extend = extend
        self.list = list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend is not None:
            result['extend'] = self.extend

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend') is not None:
            self.extend = m.get('extend')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListServiceApplyResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListServiceApplyResponseBodyDataList(DaraModel):
    def __init__(
        self,
        applier_id: str = None,
        apply_code: str = None,
        apply_component_details: List[List[str]] = None,
        apply_time: int = None,
        appointments: List[main_models.ListServiceApplyResponseBodyDataListAppointments] = None,
        buy_url: str = None,
        creator_emp_id: str = None,
        customer_name: str = None,
        cycle_service: bool = None,
        executed_count: int = None,
        finish_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_one_to_one_expert_service_by_time: bool = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        pack_details: List[Dict[str, Any]] = None,
        pay_orders: List[main_models.ListServiceApplyResponseBodyDataListPayOrders] = None,
        pay_url: str = None,
        performance_orders: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrders] = None,
        performance_packs: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacks] = None,
        rene_wal_url: str = None,
        service_code: str = None,
        service_name: str = None,
        service_reports: List[main_models.ListServiceApplyResponseBodyDataListServiceReports] = None,
        service_time_range: List[int] = None,
        status: str = None,
        status_code: int = None,
        status_str: str = None,
        term_of_validity: str = None,
        total_pack: int = None,
        type: str = None,
        use_pack: int = None,
        user_rights: str = None,
    ):
        self.applier_id = applier_id
        self.apply_code = apply_code
        self.apply_component_details = apply_component_details
        self.apply_time = apply_time
        self.appointments = appointments
        self.buy_url = buy_url
        self.creator_emp_id = creator_emp_id
        self.customer_name = customer_name
        self.cycle_service = cycle_service
        self.executed_count = executed_count
        self.finish_count = finish_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_one_to_one_expert_service_by_time = is_one_to_one_expert_service_by_time
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.pack_details = pack_details
        self.pay_orders = pay_orders
        self.pay_url = pay_url
        self.performance_orders = performance_orders
        self.performance_packs = performance_packs
        self.rene_wal_url = rene_wal_url
        self.service_code = service_code
        self.service_name = service_name
        self.service_reports = service_reports
        self.service_time_range = service_time_range
        self.status = status
        self.status_code = status_code
        self.status_str = status_str
        self.term_of_validity = term_of_validity
        self.total_pack = total_pack
        self.type = type
        self.use_pack = use_pack
        self.user_rights = user_rights

    def validate(self):
        if self.appointments:
            for v1 in self.appointments:
                 if v1:
                    v1.validate()
        if self.pay_orders:
            for v1 in self.pay_orders:
                 if v1:
                    v1.validate()
        if self.performance_orders:
            for v1 in self.performance_orders:
                 if v1:
                    v1.validate()
        if self.performance_packs:
            for v1 in self.performance_packs:
                 if v1:
                    v1.validate()
        if self.service_reports:
            for v1 in self.service_reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applier_id is not None:
            result['applierId'] = self.applier_id

        if self.apply_code is not None:
            result['applyCode'] = self.apply_code

        if self.apply_component_details is not None:
            result['applyComponentDetails'] = self.apply_component_details

        if self.apply_time is not None:
            result['applyTime'] = self.apply_time

        result['appointments'] = []
        if self.appointments is not None:
            for k1 in self.appointments:
                result['appointments'].append(k1.to_map() if k1 else None)

        if self.buy_url is not None:
            result['buyUrl'] = self.buy_url

        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.customer_name is not None:
            result['customerName'] = self.customer_name

        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service

        if self.executed_count is not None:
            result['executedCount'] = self.executed_count

        if self.finish_count is not None:
            result['finishCount'] = self.finish_count

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.is_one_to_one_expert_service_by_time is not None:
            result['isOneToOneExpertServiceByTime'] = self.is_one_to_one_expert_service_by_time

        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.pack_details is not None:
            result['packDetails'] = self.pack_details

        result['payOrders'] = []
        if self.pay_orders is not None:
            for k1 in self.pay_orders:
                result['payOrders'].append(k1.to_map() if k1 else None)

        if self.pay_url is not None:
            result['payUrl'] = self.pay_url

        result['performanceOrders'] = []
        if self.performance_orders is not None:
            for k1 in self.performance_orders:
                result['performanceOrders'].append(k1.to_map() if k1 else None)

        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k1 in self.performance_packs:
                result['performancePacks'].append(k1.to_map() if k1 else None)

        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url

        if self.service_code is not None:
            result['serviceCode'] = self.service_code

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        result['serviceReports'] = []
        if self.service_reports is not None:
            for k1 in self.service_reports:
                result['serviceReports'].append(k1.to_map() if k1 else None)

        if self.service_time_range is not None:
            result['serviceTimeRange'] = self.service_time_range

        if self.status is not None:
            result['status'] = self.status

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.status_str is not None:
            result['statusStr'] = self.status_str

        if self.term_of_validity is not None:
            result['termOfValidity'] = self.term_of_validity

        if self.total_pack is not None:
            result['totalPack'] = self.total_pack

        if self.type is not None:
            result['type'] = self.type

        if self.use_pack is not None:
            result['usePack'] = self.use_pack

        if self.user_rights is not None:
            result['userRights'] = self.user_rights

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applierId') is not None:
            self.applier_id = m.get('applierId')

        if m.get('applyCode') is not None:
            self.apply_code = m.get('applyCode')

        if m.get('applyComponentDetails') is not None:
            self.apply_component_details = m.get('applyComponentDetails')

        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')

        self.appointments = []
        if m.get('appointments') is not None:
            for k1 in m.get('appointments'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListAppointments()
                self.appointments.append(temp_model.from_map(k1))

        if m.get('buyUrl') is not None:
            self.buy_url = m.get('buyUrl')

        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')

        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')

        if m.get('executedCount') is not None:
            self.executed_count = m.get('executedCount')

        if m.get('finishCount') is not None:
            self.finish_count = m.get('finishCount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isOneToOneExpertServiceByTime') is not None:
            self.is_one_to_one_expert_service_by_time = m.get('isOneToOneExpertServiceByTime')

        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')

        self.pay_orders = []
        if m.get('payOrders') is not None:
            for k1 in m.get('payOrders'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPayOrders()
                self.pay_orders.append(temp_model.from_map(k1))

        if m.get('payUrl') is not None:
            self.pay_url = m.get('payUrl')

        self.performance_orders = []
        if m.get('performanceOrders') is not None:
            for k1 in m.get('performanceOrders'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrders()
                self.performance_orders.append(temp_model.from_map(k1))

        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k1 in m.get('performancePacks'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k1))

        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')

        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k1 in m.get('serviceReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListServiceReports()
                self.service_reports.append(temp_model.from_map(k1))

        if m.get('serviceTimeRange') is not None:
            self.service_time_range = m.get('serviceTimeRange')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')

        if m.get('termOfValidity') is not None:
            self.term_of_validity = m.get('termOfValidity')

        if m.get('totalPack') is not None:
            self.total_pack = m.get('totalPack')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('usePack') is not None:
            self.use_pack = m.get('usePack')

        if m.get('userRights') is not None:
            self.user_rights = m.get('userRights')

        return self

class ListServiceApplyResponseBodyDataListServiceReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacks(DaraModel):
    def __init__(
        self,
        apply_file_volist: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports] = None,
        service_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceReports] = None,
        service_schemes: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[main_models.ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for v1 in self.apply_file_volist:
                 if v1:
                    v1.validate()
        if self.ext_list:
            for v1 in self.ext_list:
                 if v1:
                    v1.validate()
        if self.performance_node_dtos:
            for v1 in self.performance_node_dtos:
                 if v1:
                    v1.validate()
        if self.service_month_reports:
            for v1 in self.service_month_reports:
                 if v1:
                    v1.validate()
        if self.service_reports:
            for v1 in self.service_reports:
                 if v1:
                    v1.validate()
        if self.service_schemes:
            for v1 in self.service_schemes:
                 if v1:
                    v1.validate()
        if self.tam_engineers:
            for v1 in self.tam_engineers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k1 in self.apply_file_volist:
                result['applyFileVOList'].append(k1.to_map() if k1 else None)

        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code

        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time

        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time

        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time

        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc

        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service

        result['extList'] = []
        if self.ext_list is not None:
            for k1 in self.ext_list:
                result['extList'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code

        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail

        if self.order_id is not None:
            result['orderId'] = self.order_id

        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k1 in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k1.to_map() if k1 else None)

        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k1 in self.service_month_reports:
                result['serviceMonthReports'].append(k1.to_map() if k1 else None)

        result['serviceReports'] = []
        if self.service_reports is not None:
            for k1 in self.service_reports:
                result['serviceReports'].append(k1.to_map() if k1 else None)

        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k1 in self.service_schemes:
                result['serviceSchemes'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.status_str is not None:
            result['statusStr'] = self.status_str

        if self.support_time is not None:
            result['supportTime'] = self.support_time

        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k1 in self.tam_engineers:
                result['tamEngineers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k1 in m.get('applyFileVOList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k1))

        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')

        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')

        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')

        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')

        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')

        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')

        self.ext_list = []
        if m.get('extList') is not None:
            for k1 in m.get('extList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')

        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k1 in m.get('performanceNodeDTOS'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k1))

        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k1 in m.get('serviceMonthReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k1))

        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k1 in m.get('serviceReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k1))

        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k1 in m.get('serviceSchemes'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')

        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')

        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k1 in m.get('tamEngineers'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k1))

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksTamEngineers(DaraModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status

        if self.id is not None:
            result['id'] = self.id

        if self.last_name is not None:
            result['lastName'] = self.last_name

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en

        if self.realm_id is not None:
            result['realmId'] = self.realm_id

        if self.workid is not None:
            result['workid'] = self.workid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')

        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')

        if m.get('workid') is not None:
            self.workid = m.get('workid')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksServiceSchemes(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksServiceReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksServiceMonthReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksPerformanceNodeDTOS(DaraModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['display'] = self.display

        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info

        if self.index is not None:
            result['index'] = self.index

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')

        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksExtList(DaraModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_code is not None:
            result['keyCode'] = self.key_code

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

class ListServiceApplyResponseBodyDataListPerformancePacksApplyFileVOList(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrders(DaraModel):
    def __init__(
        self,
        apply_file_volist: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        pack_count: int = None,
        pack_details: List[Dict[str, Any]] = None,
        performance_node_dtos: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS] = None,
        performance_packs: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports] = None,
        service_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports] = None,
        service_schemes: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.pack_count = pack_count
        self.pack_details = pack_details
        self.performance_node_dtos = performance_node_dtos
        self.performance_packs = performance_packs
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for v1 in self.apply_file_volist:
                 if v1:
                    v1.validate()
        if self.ext_list:
            for v1 in self.ext_list:
                 if v1:
                    v1.validate()
        if self.performance_node_dtos:
            for v1 in self.performance_node_dtos:
                 if v1:
                    v1.validate()
        if self.performance_packs:
            for v1 in self.performance_packs:
                 if v1:
                    v1.validate()
        if self.service_month_reports:
            for v1 in self.service_month_reports:
                 if v1:
                    v1.validate()
        if self.service_reports:
            for v1 in self.service_reports:
                 if v1:
                    v1.validate()
        if self.service_schemes:
            for v1 in self.service_schemes:
                 if v1:
                    v1.validate()
        if self.tam_engineers:
            for v1 in self.tam_engineers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k1 in self.apply_file_volist:
                result['applyFileVOList'].append(k1.to_map() if k1 else None)

        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code

        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time

        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time

        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time

        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc

        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service

        result['extList'] = []
        if self.ext_list is not None:
            for k1 in self.ext_list:
                result['extList'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code

        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.pack_count is not None:
            result['packCount'] = self.pack_count

        if self.pack_details is not None:
            result['packDetails'] = self.pack_details

        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k1 in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k1.to_map() if k1 else None)

        result['performancePacks'] = []
        if self.performance_packs is not None:
            for k1 in self.performance_packs:
                result['performancePacks'].append(k1.to_map() if k1 else None)

        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k1 in self.service_month_reports:
                result['serviceMonthReports'].append(k1.to_map() if k1 else None)

        result['serviceReports'] = []
        if self.service_reports is not None:
            for k1 in self.service_reports:
                result['serviceReports'].append(k1.to_map() if k1 else None)

        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k1 in self.service_schemes:
                result['serviceSchemes'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.status_str is not None:
            result['statusStr'] = self.status_str

        if self.support_time is not None:
            result['supportTime'] = self.support_time

        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k1 in self.tam_engineers:
                result['tamEngineers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k1 in m.get('applyFileVOList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k1))

        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')

        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')

        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')

        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')

        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')

        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')

        self.ext_list = []
        if m.get('extList') is not None:
            for k1 in m.get('extList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersExtList()
                self.ext_list.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')

        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('packCount') is not None:
            self.pack_count = m.get('packCount')

        if m.get('packDetails') is not None:
            self.pack_details = m.get('packDetails')

        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k1 in m.get('performanceNodeDTOS'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k1))

        self.performance_packs = []
        if m.get('performancePacks') is not None:
            for k1 in m.get('performancePacks'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks()
                self.performance_packs.append(temp_model.from_map(k1))

        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k1 in m.get('serviceMonthReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k1))

        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k1 in m.get('serviceReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports()
                self.service_reports.append(temp_model.from_map(k1))

        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k1 in m.get('serviceSchemes'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')

        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')

        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k1 in m.get('tamEngineers'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k1))

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersTamEngineers(DaraModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status

        if self.id is not None:
            result['id'] = self.id

        if self.last_name is not None:
            result['lastName'] = self.last_name

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en

        if self.realm_id is not None:
            result['realmId'] = self.realm_id

        if self.workid is not None:
            result['workid'] = self.workid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')

        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')

        if m.get('workid') is not None:
            self.workid = m.get('workid')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceSchemes(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersServiceMonthReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacks(DaraModel):
    def __init__(
        self,
        apply_file_volist: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList] = None,
        appointment_code: str = None,
        appointment_end_time: int = None,
        appointment_id: str = None,
        appointment_pass_time: int = None,
        appointment_time: int = None,
        commodity_desc: str = None,
        creator_emp_id: str = None,
        cycle_service: bool = None,
        ext_list: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        merge_solution_and_reporter_one_step: bool = None,
        modifier_emp_id: str = None,
        ntm_commodity_code: str = None,
        order_detail: Any = None,
        order_id: int = None,
        performance_node_dtos: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS] = None,
        purchase_pack_code: int = None,
        service_apply_id: int = None,
        service_month_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports] = None,
        service_reports: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports] = None,
        service_schemes: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes] = None,
        status: int = None,
        status_str: str = None,
        support_time: List[int] = None,
        tam_engineers: List[main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers] = None,
    ):
        self.apply_file_volist = apply_file_volist
        self.appointment_code = appointment_code
        self.appointment_end_time = appointment_end_time
        self.appointment_id = appointment_id
        self.appointment_pass_time = appointment_pass_time
        self.appointment_time = appointment_time
        self.commodity_desc = commodity_desc
        self.creator_emp_id = creator_emp_id
        self.cycle_service = cycle_service
        self.ext_list = ext_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.merge_solution_and_reporter_one_step = merge_solution_and_reporter_one_step
        self.modifier_emp_id = modifier_emp_id
        self.ntm_commodity_code = ntm_commodity_code
        self.order_detail = order_detail
        self.order_id = order_id
        self.performance_node_dtos = performance_node_dtos
        self.purchase_pack_code = purchase_pack_code
        self.service_apply_id = service_apply_id
        self.service_month_reports = service_month_reports
        self.service_reports = service_reports
        self.service_schemes = service_schemes
        self.status = status
        self.status_str = status_str
        self.support_time = support_time
        self.tam_engineers = tam_engineers

    def validate(self):
        if self.apply_file_volist:
            for v1 in self.apply_file_volist:
                 if v1:
                    v1.validate()
        if self.ext_list:
            for v1 in self.ext_list:
                 if v1:
                    v1.validate()
        if self.performance_node_dtos:
            for v1 in self.performance_node_dtos:
                 if v1:
                    v1.validate()
        if self.service_month_reports:
            for v1 in self.service_month_reports:
                 if v1:
                    v1.validate()
        if self.service_reports:
            for v1 in self.service_reports:
                 if v1:
                    v1.validate()
        if self.service_schemes:
            for v1 in self.service_schemes:
                 if v1:
                    v1.validate()
        if self.tam_engineers:
            for v1 in self.tam_engineers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applyFileVOList'] = []
        if self.apply_file_volist is not None:
            for k1 in self.apply_file_volist:
                result['applyFileVOList'].append(k1.to_map() if k1 else None)

        if self.appointment_code is not None:
            result['appointmentCode'] = self.appointment_code

        if self.appointment_end_time is not None:
            result['appointmentEndTime'] = self.appointment_end_time

        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.appointment_pass_time is not None:
            result['appointmentPassTime'] = self.appointment_pass_time

        if self.appointment_time is not None:
            result['appointmentTime'] = self.appointment_time

        if self.commodity_desc is not None:
            result['commodityDesc'] = self.commodity_desc

        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.cycle_service is not None:
            result['cycleService'] = self.cycle_service

        result['extList'] = []
        if self.ext_list is not None:
            for k1 in self.ext_list:
                result['extList'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.merge_solution_and_reporter_one_step is not None:
            result['mergeSolutionAndReporterOneStep'] = self.merge_solution_and_reporter_one_step

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.ntm_commodity_code is not None:
            result['ntmCommodityCode'] = self.ntm_commodity_code

        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail

        if self.order_id is not None:
            result['orderId'] = self.order_id

        result['performanceNodeDTOS'] = []
        if self.performance_node_dtos is not None:
            for k1 in self.performance_node_dtos:
                result['performanceNodeDTOS'].append(k1.to_map() if k1 else None)

        if self.purchase_pack_code is not None:
            result['purchasePackCode'] = self.purchase_pack_code

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        result['serviceMonthReports'] = []
        if self.service_month_reports is not None:
            for k1 in self.service_month_reports:
                result['serviceMonthReports'].append(k1.to_map() if k1 else None)

        result['serviceReports'] = []
        if self.service_reports is not None:
            for k1 in self.service_reports:
                result['serviceReports'].append(k1.to_map() if k1 else None)

        result['serviceSchemes'] = []
        if self.service_schemes is not None:
            for k1 in self.service_schemes:
                result['serviceSchemes'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.status_str is not None:
            result['statusStr'] = self.status_str

        if self.support_time is not None:
            result['supportTime'] = self.support_time

        result['tamEngineers'] = []
        if self.tam_engineers is not None:
            for k1 in self.tam_engineers:
                result['tamEngineers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_file_volist = []
        if m.get('applyFileVOList') is not None:
            for k1 in m.get('applyFileVOList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList()
                self.apply_file_volist.append(temp_model.from_map(k1))

        if m.get('appointmentCode') is not None:
            self.appointment_code = m.get('appointmentCode')

        if m.get('appointmentEndTime') is not None:
            self.appointment_end_time = m.get('appointmentEndTime')

        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('appointmentPassTime') is not None:
            self.appointment_pass_time = m.get('appointmentPassTime')

        if m.get('appointmentTime') is not None:
            self.appointment_time = m.get('appointmentTime')

        if m.get('commodityDesc') is not None:
            self.commodity_desc = m.get('commodityDesc')

        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('cycleService') is not None:
            self.cycle_service = m.get('cycleService')

        self.ext_list = []
        if m.get('extList') is not None:
            for k1 in m.get('extList'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList()
                self.ext_list.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mergeSolutionAndReporterOneStep') is not None:
            self.merge_solution_and_reporter_one_step = m.get('mergeSolutionAndReporterOneStep')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('ntmCommodityCode') is not None:
            self.ntm_commodity_code = m.get('ntmCommodityCode')

        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        self.performance_node_dtos = []
        if m.get('performanceNodeDTOS') is not None:
            for k1 in m.get('performanceNodeDTOS'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS()
                self.performance_node_dtos.append(temp_model.from_map(k1))

        if m.get('purchasePackCode') is not None:
            self.purchase_pack_code = m.get('purchasePackCode')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        self.service_month_reports = []
        if m.get('serviceMonthReports') is not None:
            for k1 in m.get('serviceMonthReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports()
                self.service_month_reports.append(temp_model.from_map(k1))

        self.service_reports = []
        if m.get('serviceReports') is not None:
            for k1 in m.get('serviceReports'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports()
                self.service_reports.append(temp_model.from_map(k1))

        self.service_schemes = []
        if m.get('serviceSchemes') is not None:
            for k1 in m.get('serviceSchemes'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes()
                self.service_schemes.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')

        if m.get('supportTime') is not None:
            self.support_time = m.get('supportTime')

        self.tam_engineers = []
        if m.get('tamEngineers') is not None:
            for k1 in m.get('tamEngineers'):
                temp_model = main_models.ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers()
                self.tam_engineers.append(temp_model.from_map(k1))

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksTamEngineers(DaraModel):
    def __init__(
        self,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hr_status: str = None,
        id: int = None,
        last_name: str = None,
        modifier_emp_id: str = None,
        name: str = None,
        nick_name_en: str = None,
        realm_id: int = None,
        workid: str = None,
    ):
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hr_status = hr_status
        self.id = id
        self.last_name = last_name
        self.modifier_emp_id = modifier_emp_id
        self.name = name
        self.nick_name_en = nick_name_en
        self.realm_id = realm_id
        self.workid = workid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.hr_status is not None:
            result['hrStatus'] = self.hr_status

        if self.id is not None:
            result['id'] = self.id

        if self.last_name is not None:
            result['lastName'] = self.last_name

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.name is not None:
            result['name'] = self.name

        if self.nick_name_en is not None:
            result['nickNameEn'] = self.nick_name_en

        if self.realm_id is not None:
            result['realmId'] = self.realm_id

        if self.workid is not None:
            result['workid'] = self.workid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hrStatus') is not None:
            self.hr_status = m.get('hrStatus')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastName') is not None:
            self.last_name = m.get('lastName')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nickNameEn') is not None:
            self.nick_name_en = m.get('nickNameEn')

        if m.get('realmId') is not None:
            self.realm_id = m.get('realmId')

        if m.get('workid') is not None:
            self.workid = m.get('workid')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceSchemes(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksServiceMonthReports(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksPerformanceNodeDTOS(DaraModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['display'] = self.display

        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info

        if self.index is not None:
            result['index'] = self.index

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')

        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksExtList(DaraModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_code is not None:
            result['keyCode'] = self.key_code

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformancePacksApplyFileVOList(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersPerformanceNodeDTOS(DaraModel):
    def __init__(
        self,
        display: bool = None,
        extend_info: Any = None,
        index: int = None,
        node_name: str = None,
        status: int = None,
    ):
        self.display = display
        self.extend_info = extend_info
        self.index = index
        self.node_name = node_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['display'] = self.display

        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info

        if self.index is not None:
            result['index'] = self.index

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display') is not None:
            self.display = m.get('display')

        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersExtList(DaraModel):
    def __init__(
        self,
        key_code: str = None,
        name: str = None,
        value: Any = None,
        view: str = None,
    ):
        self.key_code = key_code
        self.name = name
        self.value = value
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_code is not None:
            result['keyCode'] = self.key_code

        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyCode') is not None:
            self.key_code = m.get('keyCode')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

class ListServiceApplyResponseBodyDataListPerformanceOrdersApplyFileVOList(DaraModel):
    def __init__(
        self,
        appointment_id: str = None,
        batch_group: str = None,
        customer_id: str = None,
        file_name: str = None,
        file_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remarke: str = None,
        service_apply_id: int = None,
        status: int = None,
        url: str = None,
    ):
        self.appointment_id = appointment_id
        self.batch_group = batch_group
        self.customer_id = customer_id
        self.file_name = file_name
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remarke = remarke
        self.service_apply_id = service_apply_id
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appointment_id is not None:
            result['appointmentId'] = self.appointment_id

        if self.batch_group is not None:
            result['batchGroup'] = self.batch_group

        if self.customer_id is not None:
            result['customerId'] = self.customer_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remarke is not None:
            result['remarke'] = self.remarke

        if self.service_apply_id is not None:
            result['serviceApplyId'] = self.service_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appointmentId') is not None:
            self.appointment_id = m.get('appointmentId')

        if m.get('batchGroup') is not None:
            self.batch_group = m.get('batchGroup')

        if m.get('customerId') is not None:
            self.customer_id = m.get('customerId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remarke') is not None:
            self.remarke = m.get('remarke')

        if m.get('serviceApplyId') is not None:
            self.service_apply_id = m.get('serviceApplyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListPayOrders(DaraModel):
    def __init__(
        self,
        amount: str = None,
        compass_commodity_code: str = None,
        compass_commodity_name: str = None,
        creator_emp_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier_emp_id: str = None,
        operate: Dict[str, Any] = None,
        order_detail: Any = None,
        order_id: int = None,
        original_price: float = None,
        pay_amount: float = None,
        pay_time: str = None,
        product_name: str = None,
        rene_wal_url: str = None,
        service_content_map: Dict[str, Any] = None,
        status: int = None,
        status_str: str = None,
        support_days: int = None,
        uid: str = None,
        url: str = None,
    ):
        self.amount = amount
        self.compass_commodity_code = compass_commodity_code
        self.compass_commodity_name = compass_commodity_name
        self.creator_emp_id = creator_emp_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.modifier_emp_id = modifier_emp_id
        self.operate = operate
        self.order_detail = order_detail
        self.order_id = order_id
        self.original_price = original_price
        self.pay_amount = pay_amount
        self.pay_time = pay_time
        self.product_name = product_name
        self.rene_wal_url = rene_wal_url
        self.service_content_map = service_content_map
        self.status = status
        self.status_str = status_str
        self.support_days = support_days
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.compass_commodity_code is not None:
            result['compassCommodityCode'] = self.compass_commodity_code

        if self.compass_commodity_name is not None:
            result['compassCommodityName'] = self.compass_commodity_name

        if self.creator_emp_id is not None:
            result['creatorEmpId'] = self.creator_emp_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.modifier_emp_id is not None:
            result['modifierEmpId'] = self.modifier_emp_id

        if self.operate is not None:
            result['operate'] = self.operate

        if self.order_detail is not None:
            result['orderDetail'] = self.order_detail

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.original_price is not None:
            result['originalPrice'] = self.original_price

        if self.pay_amount is not None:
            result['payAmount'] = self.pay_amount

        if self.pay_time is not None:
            result['payTime'] = self.pay_time

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.rene_wal_url is not None:
            result['reneWalUrl'] = self.rene_wal_url

        if self.service_content_map is not None:
            result['serviceContentMap'] = self.service_content_map

        if self.status is not None:
            result['status'] = self.status

        if self.status_str is not None:
            result['statusStr'] = self.status_str

        if self.support_days is not None:
            result['supportDays'] = self.support_days

        if self.uid is not None:
            result['uid'] = self.uid

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('compassCommodityCode') is not None:
            self.compass_commodity_code = m.get('compassCommodityCode')

        if m.get('compassCommodityName') is not None:
            self.compass_commodity_name = m.get('compassCommodityName')

        if m.get('creatorEmpId') is not None:
            self.creator_emp_id = m.get('creatorEmpId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifierEmpId') is not None:
            self.modifier_emp_id = m.get('modifierEmpId')

        if m.get('operate') is not None:
            self.operate = m.get('operate')

        if m.get('orderDetail') is not None:
            self.order_detail = m.get('orderDetail')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('originalPrice') is not None:
            self.original_price = m.get('originalPrice')

        if m.get('payAmount') is not None:
            self.pay_amount = m.get('payAmount')

        if m.get('payTime') is not None:
            self.pay_time = m.get('payTime')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('reneWalUrl') is not None:
            self.rene_wal_url = m.get('reneWalUrl')

        if m.get('serviceContentMap') is not None:
            self.service_content_map = m.get('serviceContentMap')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusStr') is not None:
            self.status_str = m.get('statusStr')

        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListServiceApplyResponseBodyDataListAppointments(DaraModel):
    def __init__(
        self,
        huhang_id: int = None,
        purchase_code: int = None,
        purchase_desc: str = None,
        support_days: int = None,
        travel_days: int = None,
    ):
        self.huhang_id = huhang_id
        self.purchase_code = purchase_code
        self.purchase_desc = purchase_desc
        self.support_days = support_days
        self.travel_days = travel_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.huhang_id is not None:
            result['huhangId'] = self.huhang_id

        if self.purchase_code is not None:
            result['purchaseCode'] = self.purchase_code

        if self.purchase_desc is not None:
            result['purchaseDesc'] = self.purchase_desc

        if self.support_days is not None:
            result['supportDays'] = self.support_days

        if self.travel_days is not None:
            result['travelDays'] = self.travel_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('huhangId') is not None:
            self.huhang_id = m.get('huhangId')

        if m.get('purchaseCode') is not None:
            self.purchase_code = m.get('purchaseCode')

        if m.get('purchaseDesc') is not None:
            self.purchase_desc = m.get('purchaseDesc')

        if m.get('supportDays') is not None:
            self.support_days = m.get('supportDays')

        if m.get('travelDays') is not None:
            self.travel_days = m.get('travelDays')

        return self

