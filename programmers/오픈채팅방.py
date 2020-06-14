ENTER = "Enter"
LEAVE = "Leave"
CHANGE = "Change"

class User(object):
    
    def __init__(self, state, uuid, name=None):
        self.state = state
        self.uuid = uuid
        self.name = name
        self.is_enter = state == ENTER
        self.is_leave = state == LEAVE
        self.is_change = state == CHANGE

def solution(records):
    msg = {LEAVE: '님이 나갔습니다.', ENTER: '님이 들어왔습니다.'}
    snapshot = {}
    activity = []
    for record in records:
        user = User(*record.split())
        if not user.is_leave:
            snapshot.update({user.uuid: user.name})
        if not user.is_change:
            activity.append((user.state, user.uuid))

    return [snapshot[uuid] + msg[state] for state, uuid in activity]



if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))