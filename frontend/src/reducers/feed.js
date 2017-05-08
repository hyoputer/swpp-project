import { SET_FEED_LIST, SET_FEED } from '../actions';

const initState = {
  desiredFeedCount: 0,
  feedList: {}
};

const feedInitState = {
  contents: null,
  like: null,
  dislike: null,
  scope: null
};

const feed = (state = initState, action) => {
  switch(action.type) {
  case SET_FEED_LIST: {
    // copy existing feed to prevent redundant GET requests 
    let newFeedList = {};
    let id;
    for(id in action.list) {
      const sid = id.toString();
      if(sid in state.feedList)
        newFeedList[sid] = state.feedList[sid]; 
      else
        newFeedList[sid] = Object.assign({}, feedInitState);
    }
    return Object.assign({}, state, { feedList : newFeedList });
  }
  case SET_FEED: {
    const newFeed = {
      contents: action.feed.contents,
      like: action.feed.like,
      dislike: action.feed.dislike,
      scope: action.feed.scope
    };
    let newFeedList = Object.assign({}, state.feedList);
    newFeedList[action.id] = newFeed;
    return Object.assign({}, state, { feedList : newFeedList });
  }
  default:
    return state;
  }
};

export default feed;