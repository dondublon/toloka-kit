__all__ = [
    'TaskSuite',
    'TaskSuiteCreateRequestParameters',
    'TaskSuitesCreateRequestParameters',
    'TaskSuiteOverlapPatch',
    'TaskSuitePatch',
]
import datetime
import toloka.client.primitives.base
import toloka.client.primitives.infinite_overlap
import toloka.client.primitives.parameter
import toloka.client.task
import typing
import uuid


class TaskSuite(toloka.client.primitives.infinite_overlap.InfiniteOverlapParametersMixin, toloka.client.primitives.base.BaseTolokaObject):
    """A set of tasks assigned to a Toloker at once.

    A task suite contains one or more tasks. Tolokers are paid after completing all tasks in a task suite.

    Attributes:
        pool_id: The ID of a pool that the task suite belongs to.
        tasks: The tasks.
        reserved_for: IDs of Tolokers who have access to the task suite.
        unavailable_for: IDs of Tolokers who don't have access to the task suite.
        issuing_order_override: The priority of a task suite.
            It influences the order of assigning task suites to Tolokers in pools with the `issue_task_suites_in_creation_order` parameter set to `True`.
            Allowed range: from -99999.99999 to 99999.99999.
        mixed: [The way of grouping tasks](https://toloka.ai/docs/guide/distribute-tasks-by-pages) to create the task suite.
            * `True` — The tasks are mixed automatically using the smart mixing approach.
            * `False` — The tasks are grouped manually.

            Default value: `False`.
        traits_all_of: The task suite can be assigned to Tolokers who have all of the specified traits.
        traits_any_of: The task suite can be assigned to Tolokers who have any of the specified traits.
        traits_none_of_any: The task suite can not be assigned to Tolokers who have any of the specified traits.
        longitude: The longitude of the point on the map for the task suite.
        latitude: The latitude of the point on the map for the task suite.
        id: The ID of the task suite. Read-only field.
        remaining_overlap: The number of times left for this task suite to be assigned to Tolokers. Read-only field.
        automerged:
            * `True` — The task suite was created after [merging tasks](https://toloka.ai/docs/api/tasks).
            * `False` — There are no merged tasks in the task suite.
        created: The UTC date and time when the task suite was created. Read-only field.
    """

    @typing.overload
    def add_base_task(self, base_task: toloka.client.task.BaseTask) -> 'TaskSuite': ...

    @typing.overload
    def add_base_task(
        self,
        *,
        input_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        known_solutions: typing.Optional[typing.List[toloka.client.task.BaseTask.KnownSolution]] = None,
        message_on_unknown_solution: typing.Optional[str] = None
    ) -> 'TaskSuite': ...

    def __init__(
        self,
        *,
        infinite_overlap=None,
        overlap=None,
        pool_id: typing.Optional[str] = None,
        tasks: typing.Optional[typing.List[toloka.client.task.BaseTask]] = ...,
        reserved_for: typing.Optional[typing.List[str]] = None,
        unavailable_for: typing.Optional[typing.List[str]] = None,
        issuing_order_override: typing.Optional[float] = None,
        mixed: typing.Optional[bool] = None,
        traits_all_of: typing.Optional[typing.List[str]] = None,
        traits_any_of: typing.Optional[typing.List[str]] = None,
        traits_none_of_any: typing.Optional[typing.List[str]] = None,
        longitude: typing.Optional[float] = None,
        latitude: typing.Optional[float] = None,
        id: typing.Optional[str] = None,
        remaining_overlap: typing.Optional[int] = None,
        automerged: typing.Optional[bool] = None,
        created: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class TaskSuite.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    _infinite_overlap: typing.Optional[bool]
    _overlap: typing.Optional[int]
    pool_id: typing.Optional[str]
    tasks: typing.Optional[typing.List[toloka.client.task.BaseTask]]
    reserved_for: typing.Optional[typing.List[str]]
    unavailable_for: typing.Optional[typing.List[str]]
    issuing_order_override: typing.Optional[float]
    mixed: typing.Optional[bool]
    traits_all_of: typing.Optional[typing.List[str]]
    traits_any_of: typing.Optional[typing.List[str]]
    traits_none_of_any: typing.Optional[typing.List[str]]
    longitude: typing.Optional[float]
    latitude: typing.Optional[float]
    id: typing.Optional[str]
    remaining_overlap: typing.Optional[int]
    automerged: typing.Optional[bool]
    created: typing.Optional[datetime.datetime]


class TaskSuiteCreateRequestParameters(toloka.client.primitives.parameter.IdempotentOperationParameters):
    """Parameters for creating a task suite.

    Attributes:
        operation_id: The UUID of the operation that conforms to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
            The UUID is used if `async_mode` is `True`.

            Specify UUID to avoid accidental errors like Toloka operation duplication caused by network problems.
            If you send several requests with the same `operation_id`, Toloka performs the operation only once.
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally.
            * `False` — The request is processed synchronously.

            Default value: `True`.
        allow_defaults: Active overlap setting:
            * `True` — Use the overlap that is set in the `defaults.default_overlap_for_new_task_suites` pool parameter.
            * `False` — Use the overlap that is set in the `overlap` task suite parameter.

            Default value: `False`.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSuiteCreateRequestParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]


class TaskSuitesCreateRequestParameters(TaskSuiteCreateRequestParameters):
    """Parameters for creating task suites.

    Attributes:
        operation_id: The UUID of the operation that conforms to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
            The UUID is used if `async_mode` is `True`.

            Specify UUID to avoid accidental errors like Toloka operation duplication caused by network problems.
            If you send several requests with the same `operation_id`, Toloka performs the operation only once.
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally.
            * `False` — The request is processed synchronously.

            Default value: `True`.
        allow_defaults: Active overlap setting:
            * `True` — Use the overlap that is set in the `defaults.default_overlap_for_new_task_suites` pool parameter.
            * `False` — Use the overlap that is set in the `overlap` task suite parameter.

            Default value: `False`.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
        skip_invalid_items: Task suite validation option:
            * `True` — All valid task suites are added. If a task suite doesn't pass validation, then it is not added to Toloka.
            * `False` — If any task suite doesn't pass validation, then operation is cancelled and no task suites are added to Toloka.

            Default value: `False`.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None,
        skip_invalid_items: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSuitesCreateRequestParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]
    skip_invalid_items: typing.Optional[bool]


class TaskSuiteOverlapPatch(toloka.client.primitives.base.BaseTolokaObject):
    """Parameters for stopping assigning a task suite.

    Attributes:
        overlap: The new overlap value.
    """

    def __init__(self, *, overlap: typing.Optional[int] = None) -> None:
        """Method generated by attrs for class TaskSuiteOverlapPatch.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    overlap: typing.Optional[int]


class TaskSuitePatch(toloka.client.primitives.infinite_overlap.InfiniteOverlapParametersMixin, toloka.client.primitives.base.BaseTolokaObject):
    """Parameters for changing a task suite.

    Attributes:
        issuing_order_override: The priority of a task suite.
            It influences the order of assigning task suites to Tolokers in pools with the `issue_task_suites_in_creation_order` parameter set to `True`.
            Allowed range: from -99999.99999 to 99999.99999. Default value: 0.
        open_pool: Open the pool immediately after changing a task suite, if the pool is closed.

            Default value: `False`.
    """

    def __init__(
        self,
        *,
        infinite_overlap=None,
        overlap=None,
        issuing_order_override: typing.Optional[float] = None,
        open_pool: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSuitePatch.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    _infinite_overlap: typing.Optional[bool]
    _overlap: typing.Optional[int]
    issuing_order_override: typing.Optional[float]
    open_pool: typing.Optional[bool]
