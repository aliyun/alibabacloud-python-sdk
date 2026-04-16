# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudUpdateTaskRequest(DaraModel):
    def __init__(
        self,
        agent_group: str = None,
        agent_timeout: int = None,
        answer_rate: int = None,
        auto_complete: int = None,
        auto_start: int = None,
        auto_start_day: str = None,
        auto_start_time: str = None,
        auto_stop: int = None,
        auto_stop_day: str = None,
        auto_stop_time: str = None,
        auto_task_type: int = None,
        auto_trigger_time_strategy: str = None,
        call_limit_strategy: str = None,
        call_priority_strategy: str = None,
        call_route_strategy: int = None,
        call_strategy: str = None,
        call_variables: str = None,
        clid_property: str = None,
        cnos: str = None,
        concurrency: int = None,
        customer_clid_type: int = None,
        customer_clid_weight: str = None,
        customer_clid_weight_flag: int = None,
        customer_clids: str = None,
        customer_clids_category: int = None,
        customer_clids_group: str = None,
        customer_moh: str = None,
        customer_timeout: int = None,
        customer_voice: str = None,
        description: str = None,
        enterprise_id: int = None,
        force_end_flag: int = None,
        is_rewarm: int = None,
        ivr_id: int = None,
        ivr_name: str = None,
        max_wait_time: int = None,
        min_available_agent_count: int = None,
        name: str = None,
        owner_id: int = None,
        predict_adjust: int = None,
        quotiety: float = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retry_strategy: str = None,
        retry_strategy_only_today: int = None,
        retry_strategy_time_type: int = None,
        task_id: str = None,
        time_strategy: str = None,
        user_fields: str = None,
        warm_up_duration: int = None,
        wrapup: int = None,
    ):
        # 外呼组号；callGroupType=2时必填。注：一个外呼组可以绑定到多个任务，但只能同时运行一个任务中
        self.agent_group = agent_group
        # 座席超时时间；单位秒数，默认10秒，取值范围5 ~ 60
        self.agent_timeout = agent_timeout
        # 初始化预计客户接通率；默认50，取值范围1～100，预热阶段的呼叫，按照此接通率计算呼叫频率
        self.answer_rate = answer_rate
        # 0.关闭 1.开启，默认开启。开启：任务中的号码呼叫完后，任务自动完成，状态设置为结束，关闭：任务中的号码呼叫完后，任务自动暂停，状态设置为暂停注：任务在结束状态时无法再次启动。
        self.auto_complete = auto_complete
        # 定时开始；0.关闭 1.开启，默认关闭。值为1时autoStartDay和autoStartTime参数才生效，并且至少设置其中的一个
        self.auto_start = auto_start
        # 定时开始日期；autoStart=1时生效。参数不传入时默认在当天的autoStartTime定时启动。格式：yyyy-MM-dd，如：2017-01-01
        self.auto_start_day = auto_start_day
        # 定时开始时间；autoStart=1时生效。参数不传入时默认在autoStartDay的00:00:00定时启动。格式：HH:mm:ss，如：08:00:00
        self.auto_start_time = auto_start_time
        # 定时完成；0.关闭 1.开启，默认关闭。值为1时autoStopDay和autoStopTime参数才生效，并且至少设置其中的一个
        self.auto_stop = auto_stop
        # 定时完成日期；autoStop=1时生效。参数不传入时默认在当天的autoStopTime定时完成。格式：yyyy-MM-dd，如：2017-01-01
        self.auto_stop_day = auto_stop_day
        # 定时完成时间；autoStop=1时生效。参数不传入时默认在autoStopDay的23:59:59定时完成。格式：HH:mm:ss，如：17:00:00
        self.auto_stop_time = auto_stop_time
        # 0.连续呼叫 1.间隔呼叫，默认连续呼叫。配合定时开始（autoStart）和定时结束（autoStop）参数使用，如任务需要在每天的特定时间段内呼叫则开启间隔呼叫方式
        self.auto_task_type = auto_task_type
        # 间隔呼叫时间段；autoTaskType=1时必填。呼叫的时间段配置。参数格式：时间条件编号。支持多个，多个使用英文","逗号隔开，如：9,22。注：时间条件列表可通过查询时间条件设置列表接口获取
        self.auto_trigger_time_strategy = auto_trigger_time_strategy
        # 座席当日接听的通话个数上限，使用方式详见下方说明；JsonArray格式 [{"cnos":["2000","2001"],"limit":"5"}] 注：使用座席当日接听数限制功能需开启企业配置，功能开启并且配置上限后系统才开始统计当日接听数
        self.call_limit_strategy = call_limit_strategy
        # 数据结构为Json格式```{"strategy":[{"sort":1,"type":"retryCall", "desc":0},{"sort":2,"type":"firstCall","orderType":0}]}```格式说明：sort是重试号码和未呼叫号码的呼叫顺序 type：retryCall重试号码、firstCall未呼叫号码当type=retryCall，desc：0.优先呼叫待重呼轮次数值较小的号码，即轮次靠前（如第1轮、第2轮）的号码先被呼叫 1.优先呼叫待重呼轮次数值较大的号码，即轮次靠后（如第5轮、第4轮）的号码先被呼叫当type=firstCall时，orderType：随机呼叫，0顺序(优先级) 1随机 2顺序(导入时间)
        self.call_priority_strategy = call_priority_strategy
        # 1.直连座席 2.AI转人工 直连座席模式：客户接听后直接分配座席，无空闲座席可溢出语音导航（需配置语音导航），保障高优先级客户直连体验 AI转人工：客户接入后，优先进入语音导航中配置的智能体机器人，按交互结果决定是否转接座席，提升自动化覆盖率，降低人工成本
        self.call_route_strategy = call_route_strategy
        # 座席分配规则；1.随机 2.顺序 3.座席未进线最大时（从上一次呼叫结束到当前的总时长） 4.座席状态[空闲]最长时长（座席最近一次切换为空闲状态的持续时长），默认随机
        self.call_strategy = call_strategy
        # 座席通道变量。JsonArray格式；最大支持5个变量。默认空值， 示例：[{"name":"abcdefg","value":"${cdr_enterprise_id}"}] 注：单个字段值的长度不能超过1000个字符。变量会以SIP_HEADER的形式设置到座席侧通道
        self.call_variables = call_variables
        # 外显规则；customerClidType=2时生效。Json格式，外显号码选择规则：默认区号，是否匹配省会等；如：{"defaultAreaCode":"010", "isMatchCapital":"1"}。不建议使用
        self.clid_property = clid_property
        # 座席工号列表；callGroupType=1时必填。支持多个座席工号，多个之间使用英文逗号\\",\\"分隔注：一个座席只能在一个运行中的任务中
        self.cnos = cnos
        # 任务维度限制最大并发数，实际并发不会超过最大并发限制。type=1时，配置成0表示不限制，座席数量少于10时建议配置该参数
        self.concurrency = concurrency
        # 客户侧外显规则；customerClidsCategory=1或2时生效。1.随机 2.按区号，默认随机。不建议使用
        self.customer_clid_type = customer_clid_type
        # 外显号码比例配置内容；customerClidsCategory=1且customerClidWeightFlag=1时生效。JsonArray格式 [{"number":"123,345","weight":"5"}, {"number":"567,789","weight":"5"}]，不建议使用
        self.customer_clid_weight = customer_clid_weight
        # 外显号码比例配置开关；customerClidsCategory=1时生效。0.关闭 1.开启，默认关闭。不建议使用
        self.customer_clid_weight_flag = customer_clid_weight_flag
        # 客户侧外显号码列表；customerClidsCategory=1或2时必填。支持多个，多个直接使用英文逗号\\",\\"分隔。不建议使用
        self.customer_clids = customer_clids
        # 客户侧外显号码类型；1.外显固话 2.外显手机号 4.外显号码池 5.外显导航注：推荐使用外显导航，可以灵活调整和控制外显策略。其他类型将逐步下线
        self.customer_clids_category = customer_clids_category
        # 客户侧外显号码池名称或外显导航标识；customerClidsCategory=4或5时必填。customerClidsCategory=4时customerClidsGroup传号码池名称。customerClidsCategory=5时customerClidsGroup传外显导航标识
        self.customer_clids_group = customer_clids_group
        # 客户侧等待音；客户接听后呼叫座席，等待座席接听时播放的语音，默认为空白音。支持公共语音和企业语音，值为语音文件的path，如:60000011533526918819
        self.customer_moh = customer_moh
        # 客户超时时间；单位秒数，默认30秒，取值范围5 ~ 60
        self.customer_timeout = customer_timeout
        # 客户侧提示音；客户接听后呼转座席前播放的语音，提示音播放完成后再找座席，默认无提示音。支持公共语音和企业语音，值为语音文件的path，如:60000011533526918819
        self.customer_voice = customer_voice
        # 任务描述；需进行UTF-8格式的URLEncode编码，长度小于200字
        self.description = description
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 定时完成时强制结束任务；autoStop=1时生效。0.关闭 1.开启，默认关闭。开启配置后，当任务到定时完成时间时无论任务中的号码是否已经呼完，均将任务状态设置为结束。适用于对数据有呼叫时间限制的场景。注：任务在结束状态时无法再次启动。
        self.force_end_flag = force_end_flag
        # 暂停后重新预热；0.关闭，1开启，默认开启，任务暂停后是否需要重新预热
        self.is_rewarm = is_rewarm
        # 语音导航Id；参数ivrId和ivrName二选一，同时传入时ivrId生效，在创建自动外呼任务时ivrId或ivrName必选其一。预测外呼使用场景：如果客户接听后未在特定时间内（默认2秒）找到可用座席，通话将溢出到语音导航继续排队找座席。同时支持在呼转座席，座席未接听时也溢出到语音导航，需要开启企业配置生效自动外呼使用场景：客户接听后，转到的语音导航
        self.ivr_id = ivr_id
        # 语音导航名称；参数ivrId和ivrName二选一，同时传入时ivrId生效，在创建自动外呼任务时ivrId或ivrName必选其一。
        self.ivr_name = ivr_name
        # 座席最长等待时间；默认40秒，最小10，最大600，允许座席空闲的最大时间。任务执行过程中，如果座席平均空闲时间大于maxWaitTime，每次呼叫个数会增加
        self.max_wait_time = max_wait_time
        # 最小可用座席数；默认为10，取值范围1 ~ 10。任务内可用座席数小于当前值时，任务自动暂停，避免骚扰
        self.min_available_agent_count = min_available_agent_count
        # 任务名称；需进行UTF-8格式的URLEncode编码，长度小于50字
        self.name = name
        self.owner_id = owner_id
        # 超呼率；默认值为100，取值范围50～400
        self.predict_adjust = predict_adjust
        # 骚扰率；默认值为1，取值范围为大于0，小于等于20，支持小数，精确到小数点两位。值越小呼叫的号码越少，值越大呼叫的号码越多，座席利用率越高
        self.quotiety = quotiety
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 重试策略；「基础模式」数据结构为Json格式```{"retry":2,"strategy":[{"round":1,"time":"1-1-1"},{"round":2,"time":"2-2-2"}]}```格式说明：retry是重试次数，round是第几次重试，time是第几次重试间隔的时间：1-1-1，第一个1是天，第二个1是小时，第三个1是分钟「高级模式」高级模式需要开启「号码状态识别」服务数据结构为JsonArray格式 ```[{"condition":{"sipCause":[710,719]},"retry":1,"sort":1,"strategy":[{"round":1,"time":"0-0-10"}]},{"condition":{"sipCause":[800]},"retry":1,"sort":2,"strategy":[{"round":2,"time":"0-0-10"}]}]```格式说明：condition是重试条件，sort是重试条件的顺序，其余字段与基础模式一致 注：基础模式和高级模式的区分根据传入的参数格式自动识别。基于首次呼叫时间重试时，每轮的重试时间必须大于上一轮的时间
        self.retry_strategy = retry_strategy
        # 任务仅当天生效；0.关闭 1.开启，删除待重试的数据和待呼叫的数据 2.开启，删除待重试的数据 3.开启，删除待呼叫的数据，默认关闭
        self.retry_strategy_only_today = retry_strategy_only_today
        # 重试策略时间类型；配置重试策略时生效。 1.基于首次呼叫时间 2.基于上次呼叫时间，默认基于首次呼叫时间
        self.retry_strategy_time_type = retry_strategy_time_type
        # 外呼任务Id
        # 
        # This parameter is required.
        self.task_id = task_id
        # 禁呼时间；在特定的时间段内禁止呼叫。参数格式：时间条件编号。支持多个，多个使用英文","逗号隔开，如：9,22。注：时间条件列表可通过查询时间条件设置列表接口获取
        self.time_strategy = time_strategy
        # 任务自定义字段。JsonArray格式；数组的每个元素只支持传递一组键值对，传递多组只取第一组，如 {"key", "value"}。 默认空值，示例：[{"name":"1234"},{"name1":"12345"}] 注：单个字段值的长度不能超过1000个字符
        self.user_fields = user_fields
        # 任务预热时间；默认300秒, 取值范围60 ～ 600
        self.warm_up_duration = warm_up_duration
        # 座席整理时间；默认30秒，取值范围1～10800，整理时间会影响每次呼叫的个数，值越大，呼叫号码个数会减小
        self.wrapup = wrapup

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_group is not None:
            result['AgentGroup'] = self.agent_group

        if self.agent_timeout is not None:
            result['AgentTimeout'] = self.agent_timeout

        if self.answer_rate is not None:
            result['AnswerRate'] = self.answer_rate

        if self.auto_complete is not None:
            result['AutoComplete'] = self.auto_complete

        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.auto_start_day is not None:
            result['AutoStartDay'] = self.auto_start_day

        if self.auto_start_time is not None:
            result['AutoStartTime'] = self.auto_start_time

        if self.auto_stop is not None:
            result['AutoStop'] = self.auto_stop

        if self.auto_stop_day is not None:
            result['AutoStopDay'] = self.auto_stop_day

        if self.auto_stop_time is not None:
            result['AutoStopTime'] = self.auto_stop_time

        if self.auto_task_type is not None:
            result['AutoTaskType'] = self.auto_task_type

        if self.auto_trigger_time_strategy is not None:
            result['AutoTriggerTimeStrategy'] = self.auto_trigger_time_strategy

        if self.call_limit_strategy is not None:
            result['CallLimitStrategy'] = self.call_limit_strategy

        if self.call_priority_strategy is not None:
            result['CallPriorityStrategy'] = self.call_priority_strategy

        if self.call_route_strategy is not None:
            result['CallRouteStrategy'] = self.call_route_strategy

        if self.call_strategy is not None:
            result['CallStrategy'] = self.call_strategy

        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

        if self.clid_property is not None:
            result['ClidProperty'] = self.clid_property

        if self.cnos is not None:
            result['Cnos'] = self.cnos

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.customer_clid_type is not None:
            result['CustomerClidType'] = self.customer_clid_type

        if self.customer_clid_weight is not None:
            result['CustomerClidWeight'] = self.customer_clid_weight

        if self.customer_clid_weight_flag is not None:
            result['CustomerClidWeightFlag'] = self.customer_clid_weight_flag

        if self.customer_clids is not None:
            result['CustomerClids'] = self.customer_clids

        if self.customer_clids_category is not None:
            result['CustomerClidsCategory'] = self.customer_clids_category

        if self.customer_clids_group is not None:
            result['CustomerClidsGroup'] = self.customer_clids_group

        if self.customer_moh is not None:
            result['CustomerMoh'] = self.customer_moh

        if self.customer_timeout is not None:
            result['CustomerTimeout'] = self.customer_timeout

        if self.customer_voice is not None:
            result['CustomerVoice'] = self.customer_voice

        if self.description is not None:
            result['Description'] = self.description

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.force_end_flag is not None:
            result['ForceEndFlag'] = self.force_end_flag

        if self.is_rewarm is not None:
            result['IsRewarm'] = self.is_rewarm

        if self.ivr_id is not None:
            result['IvrId'] = self.ivr_id

        if self.ivr_name is not None:
            result['IvrName'] = self.ivr_name

        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time

        if self.min_available_agent_count is not None:
            result['MinAvailableAgentCount'] = self.min_available_agent_count

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.predict_adjust is not None:
            result['PredictAdjust'] = self.predict_adjust

        if self.quotiety is not None:
            result['Quotiety'] = self.quotiety

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retry_strategy is not None:
            result['RetryStrategy'] = self.retry_strategy

        if self.retry_strategy_only_today is not None:
            result['RetryStrategyOnlyToday'] = self.retry_strategy_only_today

        if self.retry_strategy_time_type is not None:
            result['RetryStrategyTimeType'] = self.retry_strategy_time_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.time_strategy is not None:
            result['TimeStrategy'] = self.time_strategy

        if self.user_fields is not None:
            result['UserFields'] = self.user_fields

        if self.warm_up_duration is not None:
            result['WarmUpDuration'] = self.warm_up_duration

        if self.wrapup is not None:
            result['Wrapup'] = self.wrapup

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('AgentTimeout') is not None:
            self.agent_timeout = m.get('AgentTimeout')

        if m.get('AnswerRate') is not None:
            self.answer_rate = m.get('AnswerRate')

        if m.get('AutoComplete') is not None:
            self.auto_complete = m.get('AutoComplete')

        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('AutoStartDay') is not None:
            self.auto_start_day = m.get('AutoStartDay')

        if m.get('AutoStartTime') is not None:
            self.auto_start_time = m.get('AutoStartTime')

        if m.get('AutoStop') is not None:
            self.auto_stop = m.get('AutoStop')

        if m.get('AutoStopDay') is not None:
            self.auto_stop_day = m.get('AutoStopDay')

        if m.get('AutoStopTime') is not None:
            self.auto_stop_time = m.get('AutoStopTime')

        if m.get('AutoTaskType') is not None:
            self.auto_task_type = m.get('AutoTaskType')

        if m.get('AutoTriggerTimeStrategy') is not None:
            self.auto_trigger_time_strategy = m.get('AutoTriggerTimeStrategy')

        if m.get('CallLimitStrategy') is not None:
            self.call_limit_strategy = m.get('CallLimitStrategy')

        if m.get('CallPriorityStrategy') is not None:
            self.call_priority_strategy = m.get('CallPriorityStrategy')

        if m.get('CallRouteStrategy') is not None:
            self.call_route_strategy = m.get('CallRouteStrategy')

        if m.get('CallStrategy') is not None:
            self.call_strategy = m.get('CallStrategy')

        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        if m.get('ClidProperty') is not None:
            self.clid_property = m.get('ClidProperty')

        if m.get('Cnos') is not None:
            self.cnos = m.get('Cnos')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CustomerClidType') is not None:
            self.customer_clid_type = m.get('CustomerClidType')

        if m.get('CustomerClidWeight') is not None:
            self.customer_clid_weight = m.get('CustomerClidWeight')

        if m.get('CustomerClidWeightFlag') is not None:
            self.customer_clid_weight_flag = m.get('CustomerClidWeightFlag')

        if m.get('CustomerClids') is not None:
            self.customer_clids = m.get('CustomerClids')

        if m.get('CustomerClidsCategory') is not None:
            self.customer_clids_category = m.get('CustomerClidsCategory')

        if m.get('CustomerClidsGroup') is not None:
            self.customer_clids_group = m.get('CustomerClidsGroup')

        if m.get('CustomerMoh') is not None:
            self.customer_moh = m.get('CustomerMoh')

        if m.get('CustomerTimeout') is not None:
            self.customer_timeout = m.get('CustomerTimeout')

        if m.get('CustomerVoice') is not None:
            self.customer_voice = m.get('CustomerVoice')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('ForceEndFlag') is not None:
            self.force_end_flag = m.get('ForceEndFlag')

        if m.get('IsRewarm') is not None:
            self.is_rewarm = m.get('IsRewarm')

        if m.get('IvrId') is not None:
            self.ivr_id = m.get('IvrId')

        if m.get('IvrName') is not None:
            self.ivr_name = m.get('IvrName')

        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')

        if m.get('MinAvailableAgentCount') is not None:
            self.min_available_agent_count = m.get('MinAvailableAgentCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PredictAdjust') is not None:
            self.predict_adjust = m.get('PredictAdjust')

        if m.get('Quotiety') is not None:
            self.quotiety = m.get('Quotiety')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetryStrategy') is not None:
            self.retry_strategy = m.get('RetryStrategy')

        if m.get('RetryStrategyOnlyToday') is not None:
            self.retry_strategy_only_today = m.get('RetryStrategyOnlyToday')

        if m.get('RetryStrategyTimeType') is not None:
            self.retry_strategy_time_type = m.get('RetryStrategyTimeType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TimeStrategy') is not None:
            self.time_strategy = m.get('TimeStrategy')

        if m.get('UserFields') is not None:
            self.user_fields = m.get('UserFields')

        if m.get('WarmUpDuration') is not None:
            self.warm_up_duration = m.get('WarmUpDuration')

        if m.get('Wrapup') is not None:
            self.wrapup = m.get('Wrapup')

        return self

