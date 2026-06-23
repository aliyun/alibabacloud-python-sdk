# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataQualityResultsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataQualityResultsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # 数据质量校验结果分页查询结果。
        self.paging_info = paging_info
        # API请求ID。
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataQualityResultsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_quality_results: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResults] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # 质量校验结果列表。
        self.data_quality_results = data_quality_results
        # 页码。
        self.page_number = page_number
        # 页大小。
        self.page_size = page_size
        # 总条数。
        self.total_count = total_count

    def validate(self):
        if self.data_quality_results:
            for v1 in self.data_quality_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataQualityResults'] = []
        if self.data_quality_results is not None:
            for k1 in self.data_quality_results:
                result['DataQualityResults'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_quality_results = []
        if m.get('DataQualityResults') is not None:
            for k1 in m.get('DataQualityResults'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResults()
                self.data_quality_results.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResults(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        details: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails] = None,
        id: int = None,
        rule: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule = None,
        sample: str = None,
        status: str = None,
        task_instance_id: int = None,
    ):
        # 校验结果生成时间。
        self.create_time = create_time
        # 本次校验的详情。
        self.details = details
        # 校验结果ID。
        self.id = id
        # 校验开始时，规则配置快照。
        self.rule = rule
        # 本次校验所使用的样本值。
        self.sample = sample
        # 校验结果状态：
        # - Running
        # - Error
        # - Passed
        # - Warned
        # - Critical
        self.status = status
        # 校验任务实例ID。
        self.task_instance_id = task_instance_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.status is not None:
            result['Status'] = self.status

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Rule') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRule(DaraModel):
    def __init__(
        self,
        checking_config: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig = None,
        description: str = None,
        enabled: bool = None,
        error_handlers: List[main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers] = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        sampling_config: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig = None,
        severity: str = None,
        target: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget = None,
        template_code: str = None,
    ):
        # 样本校验设置。
        self.checking_config = checking_config
        # 规则描述信息，最长500个字符。
        self.description = description
        # 规则是否启用。
        self.enabled = enabled
        # 质量规则校验问题处理器。
        self.error_handlers = error_handlers
        # 规则ID。
        self.id = id
        # 规则名称，数字、英文字母、汉字、半角全角标点符号组合，最长255个字符。
        self.name = name
        # DataWorks项目空间ID。
        self.project_id = project_id
        # 样本采集所需的设置。
        self.sampling_config = sampling_config
        # 规则对于业务的等级（对应页面上的强弱规则）：
        # - High
        # - Normal
        self.severity = severity
        # 规则所监控的对象。
        self.target = target
        # 创建规则时所引用的规则模板Code。
        self.template_code = template_code

    def validate(self):
        if self.checking_config:
            self.checking_config.validate()
        if self.error_handlers:
            for v1 in self.error_handlers:
                 if v1:
                    v1.validate()
        if self.sampling_config:
            self.sampling_config.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_config is not None:
            result['CheckingConfig'] = self.checking_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        result['ErrorHandlers'] = []
        if self.error_handlers is not None:
            for k1 in self.error_handlers:
                result['ErrorHandlers'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sampling_config is not None:
            result['SamplingConfig'] = self.sampling_config.to_map()

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingConfig') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig()
            self.checking_config = temp_model.from_map(m.get('CheckingConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        self.error_handlers = []
        if m.get('ErrorHandlers') is not None:
            for k1 in m.get('ErrorHandlers'):
                temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers()
                self.error_handlers.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SamplingConfig') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig()
            self.sampling_config = temp_model.from_map(m.get('SamplingConfig'))

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Target') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleTarget(DaraModel):
    def __init__(
        self,
        database_type: str = None,
        table_guid: str = None,
        type: str = None,
    ):
        # 表类型的数据集，表所属的数据库类型：
        # - maxcompute
        # - emr
        # - cdh
        # - hologres
        # - analyticdb_for_postgresql
        # - analyticdb_for_mysql
        # - starrocks
        self.database_type = database_type
        # 表在数据地图中的唯一ID。
        self.table_guid = table_guid
        # 监控对象类型：
        # - Table
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleSamplingConfig(DaraModel):
    def __init__(
        self,
        metric: str = None,
        metric_parameters: str = None,
        sampling_filter: str = None,
        setting_config: str = None,
    ):
        # 采样的指标名称：
        # - Count：表行数
        # - Min：字段最小值
        # - Max：字段最大值
        # - Avg：字段均值
        # - DistinctCount：字段唯一值个数
        # - DistinctPercent：字段唯一值个数与数据行数占比
        # - DuplicatedCount：字段重复值个数
        # - DuplicatedPercent：字段重复值个数与数据行数占比
        # - TableSize：表大小
        # - NullValueCount：字段为空的行数
        # - NullValuePercent：字段为空的比例
        # - GroupCount：按字段值聚合后每个值与对应的数据行数
        # - CountNotIn：枚举值不匹配行数
        # - CountDistinctNotIn：枚举值不匹配唯一值个数
        # - UserDefinedSql：通过自定义SQL做样本采集
        self.metric = metric
        # 样本采集时，所需的参数。
        self.metric_parameters = metric_parameters
        # 采样时，对不关注的数据进行二次过滤的条件，最多16777215个字符。
        self.sampling_filter = sampling_filter
        # 具体执行采样语句前，插入执行的一些运行时参数设置语句，最长1000个字符。目前只支持MaxCompute。
        self.setting_config = setting_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['Metric'] = self.metric

        if self.metric_parameters is not None:
            result['MetricParameters'] = self.metric_parameters

        if self.sampling_filter is not None:
            result['SamplingFilter'] = self.sampling_filter

        if self.setting_config is not None:
            result['SettingConfig'] = self.setting_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricParameters') is not None:
            self.metric_parameters = m.get('MetricParameters')

        if m.get('SamplingFilter') is not None:
            self.sampling_filter = m.get('SamplingFilter')

        if m.get('SettingConfig') is not None:
            self.setting_config = m.get('SettingConfig')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleErrorHandlers(DaraModel):
    def __init__(
        self,
        error_data_filter: str = None,
        type: str = None,
    ):
        # 如果是自定义SQL规则，需要用户指定SQL来过滤问题数据。
        self.error_data_filter = error_data_filter
        # 处理器类型。
        # - SaveErrorData
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_data_filter is not None:
            result['ErrorDataFilter'] = self.error_data_filter

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorDataFilter') is not None:
            self.error_data_filter = m.get('ErrorDataFilter')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfig(DaraModel):
    def __init__(
        self,
        referenced_samples_filter: str = None,
        thresholds: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds = None,
        type: str = None,
    ):
        # 有些类型的阈值需要查询出一些参考样本，然后对参考样本的值进行汇总得出进行比较的阈值，这里使用一个表达式来表示参考样本的查询方式。
        self.referenced_samples_filter = referenced_samples_filter
        # 阈值设置。
        self.thresholds = thresholds
        # 阈值计算方式：
        # - Fixed
        # - Fluctation
        # - FluctationDiscreate
        # - Auto
        # - Average
        # - Variance
        self.type = type

    def validate(self):
        if self.thresholds:
            self.thresholds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.referenced_samples_filter is not None:
            result['ReferencedSamplesFilter'] = self.referenced_samples_filter

        if self.thresholds is not None:
            result['Thresholds'] = self.thresholds.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferencedSamplesFilter') is not None:
            self.referenced_samples_filter = m.get('ReferencedSamplesFilter')

        if m.get('Thresholds') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds()
            self.thresholds = temp_model.from_map(m.get('Thresholds'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholds(DaraModel):
    def __init__(
        self,
        critical: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical = None,
        expected: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected = None,
        warned: main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned = None,
    ):
        # 严重警告的阈值设置。
        self.critical = critical
        # 期望的阈值设置。
        self.expected = expected
        # 普通警告的阈值设置。
        self.warned = warned

    def validate(self):
        if self.critical:
            self.critical.validate()
        if self.expected:
            self.expected.validate()
        if self.warned:
            self.warned.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical.to_map()

        if self.expected is not None:
            result['Expected'] = self.expected.to_map()

        if self.warned is not None:
            result['Warned'] = self.warned.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical()
            self.critical = temp_model.from_map(m.get('Critical'))

        if m.get('Expected') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected()
            self.expected = temp_model.from_map(m.get('Expected'))

        if m.get('Warned') is not None:
            temp_model = main_models.ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned()
            self.warned = temp_model.from_map(m.get('Warned'))

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsWarned(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 阈值表达式。
        # 
        # 波动率类型规则必须使用表达式方式表示波动阈值。如：
        # 
        # - 波动上升大于0.01： $checkValue > 0.01 
        # - 波动下降大于0.01：$checkValue < -0.01 
        # - 波动率绝对值：abs($checkValue) > 0.01
        # 
        # 固定值类型规则也可以使用表达式方式配置阈值，如果同时配置，表达式优先级高于Operator和Value。
        self.expression = expression
        # 比较符：
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # 阈值数值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsExpected(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 阈值表达式。
        # 
        # 波动率类型规则必须使用表达式方式表示波动阈值。如：
        # 
        # - 波动上升大于0.01： $checkValue > 0.01 
        # - 波动下降大于0.01：$checkValue < -0.01 
        # - 波动率绝对值：abs($checkValue) > 0.01
        # 
        # 固定值类型规则也可以使用表达式方式配置阈值，如果同时配置，表达式优先级高于Operator和Value。
        self.expression = expression
        # 比较符：
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # 阈值数值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsRuleCheckingConfigThresholdsCritical(DaraModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
    ):
        # 阈值表达式。
        # 
        # 波动率类型规则必须使用表达式方式表示波动阈值。如：
        # 
        # - 波动上升大于0.01： $checkValue > 0.01 
        # - 波动下降大于0.01：$checkValue < -0.01 
        # - 波动率绝对值：abs($checkValue) > 0.01
        # 
        # 固定值类型规则也可以使用表达式方式配置阈值，如果同时配置，表达式优先级高于Operator和Value。
        self.expression = expression
        # 比较符：
        # - \\>
        # - \\>=
        # - \\<
        # - \\<=
        # - !=
        # - =
        self.operator = operator
        # 阈值数值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDataQualityResultsResponseBodyPagingInfoDataQualityResultsDetails(DaraModel):
    def __init__(
        self,
        checked_value: str = None,
        referenced_value: str = None,
        status: str = None,
    ):
        # 最终用来与阈值比较的值。
        self.checked_value = checked_value
        # 使用引用的样本，用来参与CheckedValue计算的基准值。
        self.referenced_value = referenced_value
        # 最终的比较结果状态：
        # - Error
        # - Passed
        # - Warned
        # - Critical
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checked_value is not None:
            result['CheckedValue'] = self.checked_value

        if self.referenced_value is not None:
            result['ReferencedValue'] = self.referenced_value

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckedValue') is not None:
            self.checked_value = m.get('CheckedValue')

        if m.get('ReferencedValue') is not None:
            self.referenced_value = m.get('ReferencedValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

