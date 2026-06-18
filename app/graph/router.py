def approval_router(state):

    if state.get("approved"):

        return "approved"

    return "rejected"